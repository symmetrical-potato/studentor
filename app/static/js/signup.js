$(document).ready(function () {
    $('.btn').click(function(e) {
        e.preventDefault();

        $(".alert").toArray().forEach(function(e) {
            e.remove();
        });

        data = validateData();
        url = $('form').attr('action');
        console.log(data);
        console.log(url);

        $.ajax({
            url: url,
            method: 'POST',
            data: data,
            success: function(resp) {
                response = JSON.parse(resp);
                if (resp.error) {
                    $("#wrapper").append(`<div class="alert alert-danger">${resp.error}</div>`);
                } else if (resp.success) {
                    window.location = `/${url.split('/')[1]}/${resp.success}`;
                } else {
                    $("#wrapper").append(`<div class="alert alert-danger">Unknown error!</div>`);
                }
            }.bind(this),
            error: function(resp) {
                $("#wrapper").append(`<div class="alert alert-danger">Unknown error!</div>`);
            }.bind(this),
        })
    });

    $('#confirm-password').keyup(function() {

        console.log($(this).val())

        if ($(this).val() != $('#password').val()) {
            $('#confirm-password').addClass('is-invalid');
            $('.btn').prop('disabled', true);
        } else {
            $('#confirm-password').removeClass('is-invalid');
            $('.btn').prop('disabled', false);
        }
    });
});


function validateData() {
    return {
        Username: $('#username').val(),
        Email: $('#email').val(),
        Password: $('#password').val(),
    }
}