$(document).ready(function() {

    const config = {
        cur_mode: 'settings',
    }

    $('.invite').click(function(e) {
        e.preventDefault();

        console.log("STFF")

        let studentId = $(this).attr('id');
        let parts = window.location.toString().split("/");
        let eventId = parts[parts.length - 1];

        console.log(studentId, eventId);

        $.ajax({
            url: '/notifications',
            method: 'POST',
            data: {
                student_id: studentId,
                event_id: eventId,
            },
            success: function(resp) {
                let response = JSON.parse(resp);
                if (response.success) {
                    $('ok-modal').modal();
                }
                console.log(resp);
            }.bind(this),
            error: function(a, b, c) {
                console.log(a, b, c);
            }.bind(this),
        })
    })

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
                    console.log('>>>', resp);
                }.bind(this),
                error: function(resp, a, b) {
                    console.log("ERR: ", resp, a, b);
                }
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