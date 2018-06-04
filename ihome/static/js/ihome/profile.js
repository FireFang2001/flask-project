function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function() {
    // $("#form-avatar").submit(function(e){
    //     e.preventDefault();
    //     var formData = new FormData($('#form-avatar')[0]);
    //     $.ajax({
    //         url: '/user/user/',
    //         type: 'PUT',
    //         dataType: 'json',
    //         data: formData,
    //         processData: false,
    //         contentType: false,
    //         cache: false,
    //         success:function (data) {
    //             if(data.code == '200'){
    //                 $('#user-avatar').attr('src', data.url)
    //             }
    //         },
    //         error:function (data) {
    //             alert(data);
    //         }
    //     })
    // });

    $("#form-name").submit(function(e){
        e.preventDefault();
        var name = $('#user-name').val();
        $.ajax({
            url: '/user/user/',
            type: 'PUT',
            dataType: 'json',
            data: {'name': name},
            success:function (data) {
                if(data.code == '200'){
                    $('.error-msg').css('display', 'none');
                }
                if(data.code == '1007'){
                    $('.error-msg').css('display', 'block');
                }
            },
            error:function (data) {
                alert(data);
            }
        })
    });

});

$('#form-avatar').submit(function () {
    $(this).ajaxSubmit({
        url: '/user/user/',
        type: 'PUT',
        dataType: 'json',
        success:function (data) {
            if(data.code == '200'){
                $('#user-avatar').attr('src', data.url);
            }
        },
        error:function (data) {
            alert('上传失败')
        }

    });
   return false
})
