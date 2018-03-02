$(document).ready(function() {

    $('#settings').click(function() {

        $('#settings-modal').modal({keyboard: true});

        $("#settings-modal__name").val($("#comp_name").text());
        $("#settings-modal__cont").val($("#comp_cont").text());
        $("#settings-modal__desc").val($("#comp_desc").text());
    });

    $("#settings-modal__save").click(function(e) {


        e.preventDefault();

        let data = {
            Username: $("#settings-modal__name").val(),
            Contacts: $("#settings-modal__cont").val(),
            Description: $("#settings-modal__desc").val(),
        }

        let opts = {
            url: window.location,
            method: 'UPDATE',
            data: data,
            success: function() {
                $("#comp_name").text(data.Username);
                $("#comp_cont").text(data.Contacts);
                $("#comp_desc").text(data.Description);
                $('#settings-modal').modal('hide');
            }.bind(this),
            error: function(a, b, c) {
                console.log("ERR", a, b, c);
            }
        }

        $.ajax(opts);
    })





    $(".theme-link").toArray().forEach(function(el) {
        $(el).attr('href', `${window.location}/event/${$(el).attr('id')}`);
    })

    $(".add-theme-fields").click(function(e) {

        e.preventDefault();

        console.log("AAAAAAAAA")

        if ($("#new-theme").css('display') === 'none') {
            $("#new-theme").css('display', 'flex');
        } else {
            $("#new-theme").css('display', 'none');
        }
    })

    $("#add-theme").click(function(e) {

        console.log("!!!")

        e.preventDefault();
        let data = validateData();
        let url = window.location.toString() + "/event";

        console.log(data, url);
        console.log(window.location.toString())

        $.ajax({
            url: url,
            method: "POST",
            data: data,
            success: function(resp) {

                let response = JSON.parse(resp);

                if (response.success) {
                    let id = response.success;
                    let name = data.Name;
                    let desc = data.Description;
                    let diploma = data.Diploma;

                    let str = `<li class="list-group-item"><h3>${name}
                    <span class="badge"><a href="${window.location}/event/${id}">Страница проекта</a></span> </h3>
                    <div class="theme__data">
                        <h4>Описание:</h4>
                        <p>${desc}</p> 
                    </div>
                </li>`

                    let lstgroup = $('.list-grouping').toArray();
                    if (lstgroup.length == 0) {
                        $('#themes').append(`<h2>
                        Темы проектов
                    </h2>
                    <ul class="list-grouping"></ul>`);
                    }

                    $('.list-grouping').append(str);


                    
                }

                
            }.bind(this),
            error: function(resp) {
                console.log("ERR", resp);
            }.bind(this),
        })
    })
});


function validateData(){
    return {
        Name: encodeURI($("#new-theme__name").val()),
        Description: encodeURI($("#new-theme__desc").val()),
        Diploma: 1,
    }
}

function showPopup() {

}