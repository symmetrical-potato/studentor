$(document).ready(function() {
    $('.list-group-item').click(function (e){
        $('.diploma__data').toArray().forEach(element => {
            $(element).addClass('non-active');
        });

        $(e.target).children('.diploma__data').removeClass('non-active');
    });
});