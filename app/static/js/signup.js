$(document).ready(function () {
    $('.btn').click(function(e) {
        e.preventDefault();

        data = validateData();
        console.log(data);
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
    })
});


function validateData() {
    return {
        Username: $('#username').val(),
        Email: $('#email').val(),
        Password: $('#password').val(),
    }
}