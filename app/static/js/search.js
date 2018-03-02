const config = {
    mode: 'all',
}

$(document).ready(function() {

    

    $('.dropdown-item').click(function (e) {

        let mode = $(this).text();

        if (mode === 'Дипломные проекты') {
            config.mode = 'dip'
        } else if (mode === 'Стажировки') {
            config.mode = 'vac'
        } else {
            config.mode = 'all'
        }

        $('.dropdown-toggle').text(mode);

        let query = $("#search-input-field").val();
        
        if (query.length >= 3) {
            makeAjaxCall($("#search-input-field").val());
        }
        
    });

    $("#search-input-field").keyup(function(e) {

        console.log("!!!!!!!");

        let query = $("#search-input-field").val();

        console.log(query);

        if (query.length >= 3) {
            reloadResults(makeAjaxCall(query));
        }

    });
});

function makeAjaxCall(query) {
    $.ajax({
        url: `/search/api?q=${query}`,
        method: 'GET',
        success: reloadResults,
        error: function(a, p, r) {
            console.log("ERR", a, p, r);
        }
    })
}

function reloadResults(data) {
    console.log('>>>', data);

    const parsed = JSON.parse(data);

    console.log(parsed[0]);

    $('.search-result').toArray().forEach(element => {
        $(element).remove();
    });

    const sorted = parsed.sort((a, b) => {
        if (a.id >= b.id) {
            return -1;
        } else {
            return 1;
        }
    });

    const filtered = sorted.filter(el => {

        console.log(el.type);
        console.log(el.type == 1);
        console.log(el.type == 2);

        if (config.mode === 'vac') {
            return el.type == 2
        } else if (config.mode === 'dip') {
            return el.type == 1
        }

        return true;
    });

    for (let index = 0; index < filtered.length; index++) {
        const element = filtered[index];
        const new_li = ` <div class="row search-result">
        <div class="col-lg-7 result-col">
            <div class="desc">
                <h2>${element.name} | <a href="/empl/${element.company_id}">${element.company_name}</a></h2>
                <a href="/empl/${element.company_id}/event/${element.id}">Ссылка на проект</a>
                <div class="project-data">
                    <p>${element.description}</p>
                </div>
            </div>
            <div class="wrapper">
                <div class="inner-wrapper">
                    ${element.type == '1' ? 'Дипломный проект' : 'Стажировка'}
                </div>
            </div>
        </div>
    </div>`

        $("#search-results").append(new_li);
    }


}