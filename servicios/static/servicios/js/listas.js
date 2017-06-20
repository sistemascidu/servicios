$(function() {
    // agregar eventos
    $("#id_term").keyup(filterTable);
});

function filterTable() {
  // Declare variables 
  var filter, tr, i;
  filter = $("#id_term").val().toUpperCase();
  tr = $("#result_list tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 1; i < tr.length; i++) {
    if (filter) {
      var found = (tr[i].outerText.toUpperCase().indexOf(filter) >= 0);
      tr[i].style.display = (found) ? "" : "none";
    }
    else{
      tr[i].style.display = "";
    }
  }
}