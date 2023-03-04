var highscoreSaveApiUrl = 'http://127.0.0.1:51000/insertHighscore';
var highscoreListApiUrl = 'http://127.0.0.1:51000/getHighscores';


$(function () {
    $.get(highscoreListApiUrl, function (response) {
        if(response) {
            var table = '';
            $.each(response, function(index, highscores) {
                table += '<tr>' +
                    '<td>'+ highscores.player_id +'</td>'+
                    '<td>'+ highscores.player_name +'</td>'+
                    '<td>'+ highscores.score +'</td>'+
                    '<td>'+ highscores.datetime +'</td></tr>';
            });
            $("table").find('tbody').empty().html(table);
        }
    });
});

$("#saveHighscore").on("click", function () {
        var data = $("#productForm").serializeArray();
        var requestPayload = {
            player_name: null,
            score: null,
            datetime: null
        };
        for (var i=0;i<data.length;++i) {
            var element = data[i];
            switch(element.name) {
                case 'name':
                    requestPayload.player_name = element.value;
                    break;
                case 'score':
                    requestPayload.score = element.value;
                    break;
                case 'datetime':
                    requestPayload.datetime = element.value;
                    break;
            }
        }
        callApi("POST", highscoreSaveApiUrl, {
            'data': JSON.stringify(requestPayload)
        });
    });