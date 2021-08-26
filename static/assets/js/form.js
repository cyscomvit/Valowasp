// Select all the members
const memberContainer = document.querySelectorAll(".memberContainer");

// count the number from the dropdown
var e = document.getElementById("Totalmembers");
function numberSelected() {
  var strUser = e.options[e.selectedIndex].value;
  containerSelected(strUser);
}

// turn display form none=>block
function containerSelected(num) {
  for (var i = 0; i < num; i++) {
    memberContainer[i].style.display = "block";
  }
}
e.onchange = numberSelected;
numberSelected();
