var infobtn = document.getElementById("infobtn");
var head_img = document.getElementById("head_img");
var idfront = document.getElementById("idfront");
var idbehind = document.getElementById("idbehind");
var rnbtn = document.getElementById("rnbtn");
$(function () {

});
infobtn.onclick = function () {
    var Data = new FormData();
    if (head_img.files.length !== 0)
        Data.append("head_img", head_img.files[0]);
    if ($("#account").val() !== "")
        Data.append("account", $("#account").val());
    $.ajax({
        url: url + '/post/modify_p_info/',
        type: "POST",
        data: Data,
        cache: false,         //不设置缓存
        processData: false,  // 不处理数据
        contentType: false,   // 不设置内容类型
        beforeSend: function () {
            $("#infoloading").css("display","block");
        },
        success: function (data) {
            $("#infoloading").css("display","none");
            if (data.status === 'true') {
                $("#infoerr").css("display", "none");
                $("#infosuccess").text("保存成功").css("display", "block");
            }
        },
        error: function () {
            $("#infoloading").css("display","block");
            $("#infosuccess").text("服务器错误").css("display", "block");
        }
    });
}
rnbtn.onclick = function () {
    var sex = $("#sex").val();
    var age = $("#age").val();
    var name = $("#name").val();
    var idnumber = $("#idnumber").val();
    var phone = $("#phone").val();
    if (sex === "" || age === "" || name === "" || idnumber === "" || phone === "" || idfront.files.length === 0 || idbehind.files.length === 0) {
        $("#rnsuccess").css("display", "none");
        $("#rnerr").text("请填写完整信息").css("display", "block");

    } else if (!(/^1(3|4|5|6|7|8|9)\d{9}$/.test(phone))) {
        $("#rnsuccess").css("display", "none");
        $("#rnerr").text("手机号不符合规范").css("display", "block");
    } else if(!(/^[0-9]{18}/).test(idnumber)) {
         $("#rnsuccess").css("display", "none");
        $("#rnerr").text("身份证应是18位").css("display", "block");
    } else {
        var data = new FormData();
        data.append("sex", sex);
        data.append("age", age);
        data.append("idnumber", idnumber);
        data.append("name", name);
        data.append("phone", phone);
        data.append("idfront", idfront.files[0]);
        data.append("idbehind", idbehind.files[0]);
        $.ajax({
        url: url + '/post/realname/',
        type: "POST",
        data: data,
        cache: false,         //不设置缓存
        processData: false,  // 不处理数据
        contentType: false,   // 不设置内容类型
        beforeSend: function () {
            $("#rnloading").css("display","block");
        },
        success: function (data) {
            $("#rnloading").css("display","none");
            if (data.status === 'true') {
                $("#rnerr").css("display", "none");
                $("#rnsuccess").text("上传成功等待管理员审核").css("display", "block");
            }
        },
        error: function () {
            $("#rnloading").css("display","none");
            $("#rnerr").text("服务器错误").css("display", "block");
        }
    });
    }


}