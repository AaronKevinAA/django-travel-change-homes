
var loginbtn = document.getElementById("loginbtn");
var exitbtn = document.getElementById("exit_login");
var registerbtn = document.getElementById("registerbtn");
$(document).ready(function(){
    if(path.match('/pinfo/') ){
        $('#li_home').removeClass('active');
        $('#li_pinfo').addClass('active');
    }
    $('#loginerr').css("display","none");
    user = $.cookie('user_email');
    if(typeof (user) =="undefined"){
        $('#li_login').css("display","block");
        $('#exit_login').css("display","none");
        $('#user_email').css("display","none");
        $('#li_pinfo').css("display","none");
    }else{
        $('#li_login').css("display","none");
        $('#li_pinfo').css("display","block");
        $('#exit_login').css("display","block");
        $('#user_email').html(user);
    }


});
// 退出登陆
exitbtn.onclick = function(){
     $.ajax({
         url: url + '/post/exit_login/',
         data: JSON.stringify({
             "email": user,
         }),
         type: 'post',
         contentType: "json/application",
         dataType: 'json',
         success: function (data) {
             if (data.status === 'false') {
             } else {
                 $.removeCookie('user_email',{ path: '/' });
                 location.replace(url);
             }
             console.log(data.err);
         },
         error: function () {
             console.log('ajax请求失败！');
         }
     });
}
// 登陆
loginbtn.onclick = function () {
    var email = $("#loginemail").val();
    var password = $("#loginpwd").val();

       $.ajax({
        url: url+'/post/login/',
        data: JSON.stringify({
            "email":email,
            "password":password,
        }),
        type: 'post',
        contentType:"json/application",
        dataType: 'json',
        beforeSend: function () {
            $("#loginloading").css("display","block");
        },
        success: function (data) {
            $("#loginloading").css("display","none");
            if(data.status==='false'){
                $("#loginerr").text(data.err+",请重新输入").css("display","block");
            }else{
                $.cookie('user_email', email,{ path: '/' });
                location.replace(url);
            }
        },
        error: function () {
            $("#loginloading").css("display","none");
            $("#loginerr").text("服务器错误").css("display","block");
        }
    });
}
// 注册
registerbtn.onclick = function () {
    var email = $("#reemail").val();
    var password = $("#repwd").val();
    var cpassword = $("#recpwd").val();
    var emailReg=/^[a-zA-Z0-9_-]+@([a-zA-Z0-9]+\.)+(com|cn|net|org)$/;
    if(email===""||password===""||cpassword==="")
    {
        $("#reerr").text("请完整填写信息").css("display","block");
    }else if(!emailReg.test(email)){
        $("#reerr").text("邮箱格式不正确").css("display","block");
    }else if(password!==cpassword){
        $("#reerr").text("两次输入密码不一致").css("display","block");
    }
    else{
        $.ajax({
        url: url+'/post/register/',
        data: JSON.stringify({
            "email":email,
            "password":password,
        }),
        type: 'post',
        contentType:"json/application",
        dataType: 'json',
        beforeSend:function(){
            $("#registerloading").css("display","block");
        },
        success: function (data) {
            $("#registerloading").css("display","none");
            if(data.status==='false'){
                $("#reerr").text(data.err).css("display","block");
            }else{
                $("#reerr").css("display","none");
                $("#resuccess").text("注册成功").css("display","block");
            }
        },
        error: function () {
             $("#registerloading").css("display","none");
            console.log('ajax请求失败！');
        }
    });
    }
}