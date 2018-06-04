function hrefBack() {
    history.go(-1);
}

function decodeQuery(){
    var search = decodeURI(document.location.search);
    return search.replace(/(^\?)/, '').split('&').reduce(function(result, item){
        values = item.split('=');
        result[values[0]] = values[1];
        return result;
    }, {});
}

// $(document).ready(function(){
//     var mySwiper = new Swiper ('.swiper-container', {
//         loop: true,
//         autoplay: 2000,
//         autoplayDisableOnInteraction: false,
//         pagination: '.swiper-pagination',
//         paginationType: 'fraction',
//     });
//     $(".book-house").show();
// });

$(document).ready(function () {
    var path = location.search;
    var id = path.split('=')[1];
    $.get('/house/detail/' + id + '/', function (data) {
        if (data.code == '200'){
            var detail_house = template('house_detail_list', {ohouse: data.house, facilities: data.facilities});
            $('.container').append(detail_house);

            var mySwiper = new Swiper ('.swiper-container', {
                loop: true,
                autoplay: 2000,
                autoplayDisableOnInteraction: false,
                pagination: '.swiper-pagination',
                paginationType: 'fraction',
            });
            $(".book-house").show();
            if(!data.booking) {
                $('.book-house').click(function(){
                $('.theme-popover-mask').fadeIn(100);
                $('.theme-popover').slideDown(200);
              });
                $('.theme-poptit .close').click(function(){
                    $('.theme-popover-mask').fadeOut(100);
                    $('.theme-popover').slideUp(200);
                });
            }else if (data.booking == 1) {
                $(".book-house").click(function () {
                    location.href='/house/booking/?id='+data.house.id
                });
            }else {
                $(".book-house").hide();
            }
            // if (data.booking){
            //     $(".book-house").show();
            // } else {
            //     $(".book-house").hide();
            // }
        }

    });
    $('.theme-signin').submit(function (e) {
        e.preventDefault();
        mobile = $("#mobile").val();
        passwd = $("#password").val();
        $.post('/user/login/', {'mobile': mobile, 'password': passwd}, function (data) {
            if (data.code == '200'){
                location.reload();
            }
        });
    })
});
