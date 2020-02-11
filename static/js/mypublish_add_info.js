var addbtn = document.getElementById("addbtn");
var images = document.getElementById("images");

$(function () {
    $('#start_date').datetimepicker({
        format: 'YYYY-MM-DD',
        locale: 'zh-CN'
    });
    $('#end_date').datetimepicker({
        format: 'YYYY-MM-DD',
        locale: 'zh-CN'
    });
});
addbtn.onclick = function () {
    var facilities= '';
    if($("#wifi").is(':checked'))
        facilities += 'wifi';
    if($("#tv").is(':checked'))
        facilities += '、电视机';
    if($("#shower").is(':checked'))
        facilities += '、淋浴';
    var home_name = $("#home_name").val();
    var title = $("#title").val();
    var situation_desc = $("#situation_desc").val();
    var price = $("#price").val();
    var start_date = $("#start_date").val();
    var end_date = $("#end_date").val();
    var role = $("#role").val();
    if(home_name===0||title===""||start_date===""||end_date===""||images.files.length===0||price==='')
    {
        $("#adderr").text("请填写完整信息").css("display","block");
    }else{
        var data = new FormData();
        data.append('title',title);
        data.append('home_name',home_name);
        data.append('role',role);
        data.append('price',price);
        data.append('situation_desc',situation_desc);
        data.append('facilities',facilities);
        data.append('start_date',start_date);
        data.append('end_date',end_date);
        for(var i=0;i<images.files.length;i++)
            data.append('images[]',images.files[i]);
        $.ajax({
        url: url + '/post/publish_add/',
        type: "POST",
        data: data,
        cache: false,         //不设置缓存
        processData: false,  // 不处理数据
        contentType: false,   // 不设置内容类型
        beforeSend: function () {
            $("#addloading").css("display","block");
        },
        success: function (data) {
            $("#addloading").css("display","none");
            if (data.status === 'true') {
                $("#adderr").css("display", "none");
                $("#addsuccess").text("上传成功").css("display", "block");
            }
            console.log(data);
        },
        error: function () {
            $("#addloading").css("display","none");
            $("#adderr").text("服务器错误").css("display", "block");
        }
    });
    }
}