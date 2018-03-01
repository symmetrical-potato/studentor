$(document).ready(function() {

    const config = {
        cur_mode: 'settings',
    }

    $("#change-project").click(function(e) {
        
        let mode = $('.material-icons').text();

        e.preventDefault();
        console.log("!!!!");

        let tochange = mode === 'settings' ? 'save' : 'settings';
        config.cur_mode = tochange;
        let newDisp = mode === 'settings' ? 'block' : 'none';

        if (mode === 'save') {
            $.ajax({
                url: window.location,
                method: 'UPDATE',
                data: {
                    Name: $('.changeable#h1').text(),
                    Description: $('.changeable#p').text(),
                },
                success: function(resp) {
                    console.log(resp);
                }.bind(this),
            })
        }
 
        $('.material-icons').text(tochange);

        $(".h1-changeable-input").css('display', newDisp);
        $(".h1-changeable-input").val($('.changeable#h1').text());

        $(".p-changeable-input").css('display', newDisp);
        $(".p-changeable-input").val($('.changeable#p').text());


    });

    $("input, textarea").keyup(function (e) {

        let tochange = `.changeable#${$(this).attr('class').split('-')[0]}`;
        let newText = $(this).val();

        console.log(tochange);
        console.log(newText);
        $(tochange).text(newText);
    })
});