var upbtn = document.getElementById("upbtn");
var prove = document.getElementById("prove");
upbtn.onclick = function () {
    var name = $("#name").val();
    var area = $("#area").val();
    var location = $("#location").val();
    var type1 = $("#type1").val();
    var type2 = $("#type2").val();
    if(name===''||area===''||location===''||type1===''||type2===''||prove.files.length===0){
        $("#upsuccess").css("display", "none");
        $("#uperr").text("请填写完整信息").css("display", "block");
    }else{
        var data = new FormData();
        data.append('name',name);
        data.append('area',area);
        data.append('location',location);
        data.append('type',type1+"室"+type2+"厅");
        data.append('prove',prove.files[0]);
        $.ajax({
        url: url + '/post/home_add/',
        type: "POST",
        data: data,
        cache: false,         //不设置缓存
        processData: false,  // 不处理数据
        contentType: false,   // 不设置内容类型
        beforeSend: function () {
            $("#uploading").css("display","block");
        },
        success: function (data) {
            $("#uploading").css("display","none");
            if (data.status === 'true') {
                $("#uperr").css("display", "none");
                $("#upsuccess").text("上传成功等待管理员审核").css("display", "block");
            }
        },
        error: function () {
            $("#uploading").css("display","none");
            $("#uperr").text("服务器错误").css("display", "block");
        }
    });
    }
}