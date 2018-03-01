$(document).ready(function() {
    $('.list-group-item').click(function (e){

        console.log("!!!!!!");
        console.log($(e.target))
        console.log($(this));

        data = $($(this).children('.diploma__data'));

        if (data.css('display') === 'none') {
            data.show(400);
            data.css('display', 'block');
        } else {
            data.hide(300);
            setTimeout(() => {
                data.css('display', 'none');    
            }, 300);
        }
    });
});