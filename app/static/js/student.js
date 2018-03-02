$(document).ready(function() {
    $('.list-group-item').click(function (e){

        console.log("!!!!!!");
        console.log($(e.target).attr('class'));
        console.log($(this));

        
        if ($(e.target).attr('class') != "hide__stuff") {
            data = $($(this).children('.diploma__data'));

            if (data.css('display') === 'none') {
                data.show(400);
                data.css('display', 'block');
            }
        }
        
    });

    $('.hide__stuff').click(function (e){
        console.log('>>>parent', $(this).parent());

        let parent = $(this).parent();
        $(parent).hide(250);
    });
});