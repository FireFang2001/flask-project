function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function() {

    $("#mobile").focus(function(){
        $("#mobile-err").hide();
    });
    $("#password").focus(function(){
        $("#password-err").hide();
    });
    $(".form-login").submit(function(e){
        e.preventDefault();
        mobile = $("#mobile").val();
        passwd = $("#password").val();
        // if (!mobile) {
        //     $("#mobile-err span").html("请填写正确的手机号！");
        //     $("#mobile-err").show();
        //     return;
        // }
        // if (!passwd) {
        //     $("#password-err span").html("请填写密码!");
        //     $("#password-err").show();
        //     return;
        // }
        $.ajax({
            url: '/user/login/',
            type: 'POST',
            dataType: 'json',
            data: {'mobile': mobile, 'password': passwd},
            success:function (data) {
                if(data.code == '200'){
                    // var path = document.referrer;
                    // if(path.indexOf('/user/register') != -1 | path=='' | path.indexOf('http://127.0.0.1:8000') == -1){
                    //     location.href='/index/';
                    // } else {
                    //     location.href=path;
                    // }
                }
            },
            error:function (data) {
                alert(data);
            }
        })
    });
})