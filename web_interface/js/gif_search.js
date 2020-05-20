//Contains the basic script for the UI of a search bar
var entryField = document.getElementById("input_field");
var outputDisplay = document.getElementById("results");
var search_url = 'http://127.0.0.1:5000/query';
var search_term = "";

$(document).ready(function () {
    $("#input_field").keydown(function(e) {
			if(e.keyCode == 13){
				SearchGIFs();
        entryField.value = ''
			}
    });
});

function SearchGIFs()
{
  var query = entryField.value;
  /*
  $.ajax({
    type: "POST",
    url: search_url,
    data : {
      id: 1,
      search: 'test',
    },
    success:
    contentType: "application/json",
  });
  */
  //{search: 'test'},
  $.post(search_url,
     'test',
     function(result){
      outputDisplay.innerText = "Suggestions: " + result;
  });
}
