//Contains the basic script for the UI of a search bar
var entryField = document.getElementById("input_field");
var outputDisplay = document.getElementById("results");
var outputGIF1 = document.getElementById("result1");
var outputGIF2 = document.getElementById("result2");
var outputGIF3 = document.getElementById("result3");

var search_url = 'http://127.0.0.1:5000/query';

document.addEventListener("keydown", function (e) {
  if(e.keyCode == 13){
    SearchGIFs();
    entryField.value = ''
  }
});

function SearchGIFs()
{
  var query = entryField.value;
  var send_data = JSON.stringify({id: 1, search: query})
  console.log(send_data);

  var xmlhttp = new XMLHttpRequest();
  xmlhttp.open('POST', search_url);
  xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xmlhttp.onload = function(){
    if (xmlhttp.status === 200) {
      UpdateDisplay(JSON.parse(xmlhttp.responseText));

    }
    else {
        console.log('Request failed;  Returned status of ' + xhr.status);
    }
  };
  xmlhttp.send(send_data);
}

function UpdateDisplay(results)
{
  outputDisplay.innerText = "Suggestions: " + results.results[0].result_title;
  outputGIF1.src = 'static/gifs/' + results.results[0].result_filename;
  outputGIF2.src = 'static/gifs/' + results.results[1].result_filename;
  outputGIF3.src = 'static/gifs/' + results.results[2].result_filename;
}
