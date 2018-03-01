$(document).ready(function() {


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

        $.ajax({
            url: window.location + "/event",
            method: "POST",
            data: data,
            success: function(resp) {

                let response = JSON.parse(resp);

                if (response.success) {
                    let id = response.success;
                    let name = data.Name;
                    let desc = data.Description;
                    let diploma = data.Diploma;
                    $('.list-grouping').append(`<li class="list-group-item">${name}
                    <span class="badge"><a href="${window.location}/event/${id}">Страница проекта</a></span> </h3>
                    <div class="theme__data">
                        <h4>Описание:</h4>
                        <p>${desc}</p> 
                    </div>
                </li>`)


                    
                }

                
            }.bind(this)
        })
    })
});


function validateData(){
    return {
        Name: $("#new-theme__name").val(),
        Description: $("#new-theme__desc").val(),
        Diploma: $("#new-theme__isdiploma").prop('checked') ? 1 : 0,
    }
}