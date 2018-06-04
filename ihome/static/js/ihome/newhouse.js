function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    // $('.popup_con').fadeIn('fast');
    // $('.popup_con').fadeOut('fast');
    $.get('/house/area_facility/', function (data) {
        var area_html_list = '';

        for (var i=0; i<data.area_list.length; i++){
            var area_html = '<option value="' + data.area_list[i].id + '">' + data.area_list[i].name + '</option>';
            area_html_list += area_html;
        }
        $('#area-id').html(area_html_list);

        var facility_html_list = '';
        for (var i=0; i<data.facility_list.length; i++){
            var facility_html = '<li><div class="checkbox"><label>';
            facility_html += '<input type="checkbox" name="facility" value="' + data.facility_list[i].id + '">';
            facility_html += data.facility_list[i].name;
            facility_html += '</label></div></li>';
            facility_html_list += facility_html;
        }
        $('.house-facility-list').html(facility_html_list);
    })
});

// $('#form-house-info').submit(function () {
//    $.post('/house/newhouse/', $(this).serialize(), function (data) {
//
//    })
// });

$('#form-house-info').submit(function () {
    $(this).ajaxSubmit({
        url: '/house/newhouse/',
        type: 'POST',
        dataType: 'json',
        success:function (data) {
            if(data.code == '200'){
                $('#form-house-info').hide();
                $('#form-house-image').show();
                $('#house-id').val(data.house_id)
            }else {
                alert('a')
            }
        },
        error:function (data) {
            alert('上传失败1')
        }

    });
   return false
});

$('#form-house-image').submit(function () {
    $(this).ajaxSubmit({
        url: '/house/house_img/',
        type: 'POST',
        dataType: 'json',
        success:function (data) {
            if(data.code == '200'){
                $('.house-image-cons').append('<img src="' + data.image_url + '">')
            }else {
                $('.house-image-cons').append('<span>上传失败</span>')
            }
        },
        error:function (data) {
            alert('上传失败2')
        }

    });
   return false
});
