function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

$.get('/user/auths/', function (data) {
   if(data.code == 200){
       $('#rl_name').html('<label for="real-name">真实姓名</label><br>' + data.id_name);
       $('#id_num').html('<label for="real-name">身份证号码</label><br>' + data.id_card);
       $('.btn-success').hide();
   }
});

$(document).ready(function () {
    $('#form-auth').submit(function (e) {
        e.preventDefault();
        var real_name = $('#real-name').val();
        var id_num = $('#id-card').val();
        $.ajax({
            url: '/user/auths/',
            type: 'POST',
            dataType: 'json',
            data: {'real_name': real_name, 'id_num': id_num},
            success:function (data) {
                if(data.code == 200){
                    $('#rl_name').html('<label for="real-name">真实姓名</label><br>' + real_name);
                    $('#id_num').html('<label for="real-name">身份证号码</label><br>' + id_num);
                    $('.btn-success').hide();
                    $('.error-msg').hide();
                }else {
                    $('.error-msg').html('<i class="fa fa-exclamation-circle"></i>' + data.msg);
                    $('.error-msg').show();
                }
            },
            error:function (data) {
                alert(data)
            }
        })
    })
});