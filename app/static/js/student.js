$(document).ready(function () {
    $('.list-group-item').click(function (e) {

        // console.log("!!!!!!");
        // console.log($(e.target).attr('class'));
        // console.log($(this));


        if ($(e.target).attr('class') != "hide__stuff") {
            data = $($(this).children('.diploma__data'));

            if (data.css('display') === 'none') {
                data.show(400);
                data.css('display', 'block');
            }
        }

    });

    $('.hide__stuff').click(function (e) {
        console.log('>>>parent', $(this).parent());

        let parent = $(this).parent();
        $(parent).hide(250);
    });

    $('.remove__stuff').click(function (e) {
        console.log('try to remove item from list');
        let id = $(this).attr('data-id');
        let item = $('li[data-id="' + id + '"]');
        $.ajax({
            url: "/remove_diploma/" + id,
            method: 'PATCH',
            success: function() {
                $(item).remove();
            }
        }).fail(function () {
           alert('He удалось удалить диплом!');
        });
    });

    $("#upload_diploma").on('change', function () {
        if ($(this)[0].files[0] === undefined ||
            $(this)[0].files[0] === null)
            return;

        let form_data = new FormData();
        let id = $(this).attr('data-id');
        form_data.append("file", $(this)[0].files[0]);
        $.ajax({
            url: "/upload_diploma/" + id,
            data: form_data,
            cache: false,
            contentType: false,
            processData: false,
            method: 'POST',
            success: function (data) {
                alert('Успех!');
            }
        }).fail(function (reason) {
            alert(reason.responseText);
        });
    });
});