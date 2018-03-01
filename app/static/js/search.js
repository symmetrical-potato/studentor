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
        
        if (query.length > 5) {
            makeAjaxCall($("#search-input-field").val());
        }
        
    });

    $("#search-input-field").keyup(function(e) {

        console.log("!!!!!!!");

        let query = $("#search-input-field").val();

        console.log(query);

        if (query.length > 5) {
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

    $('.search-result').toArray().forEach(element => {
        $(element).remove();
    });

    const sorted = parsed.sort((a, b) => {
        if (a[6] >= b[6]) {
            return -1;
        } else {
            return 1;
        }
    });

    const filtered = sorted.filter(el => {

        console.log(el[5]);
        console.log(el[5] == 1);
        console.log(el[5] == 2);

        if (config.mode === 'vac') {
            return el[5] == 2
        } else if (config.mode === 'dip') {
            return el[5] == 1
        }



        return true;
    });

    for (let index = 0; index < filtered.length; index++) {
        const element = filtered[index];
        const new_li = ` <div class="row search-result">
        <div class="col-lg-7 result-col">
            <div class="desc">
                <h2>${element[0]} | <a href="/empl/${element[1]}">${element[2]}</a></h2>
                <a href="/empl/${element[1]}/event/${element[3]}">Ссылка на проект</a>
                <div class="project-data">
                    <p>${element[4]}</p>
                </div>
            </div>
            <div class="wrapper">
                <div class="inner-wrapper">
                    ${element[5] == '1' ? 'Дипломный проект' : 'Стажировка'}
                </div>
            </div>
        </div>
    </div>`

        $("#search-results").append(new_li);
    }


}