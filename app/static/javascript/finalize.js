var button = document.getElementById("finalize");
document.getElementById("results").style.display = "none";

button.onclick = function() {
  var tot = 0;

  var e = document.getElementById("q1");
  var result = e.options[e.selectedIndex].value;
  tot += parseInt(result);
  console.log(result);

  var e = document.getElementById("q2");
  var result = e.options[e.selectedIndex].value;
  tot += parseInt(result);
  console.log(result);

  var e = document.getElementById("q3");
  var result = e.options[e.selectedIndex].value;
  tot += parseInt(result);
  console.log(result);

  var e = document.getElementById("q4");
  var result = e.options[e.selectedIndex].value;
  tot += parseInt(result);
  console.log(result);

  var e = document.getElementById("q5");
  var result = e.options[e.selectedIndex].value;
  tot += parseInt(result);
  console.log(result);

  var e = document.getElementById("q6");
  var result = e.options[e.selectedIndex].value;
  tot += parseInt(result);
  console.log(result);

  var e = document.getElementById("q7");
  var result = e.options[e.selectedIndex].value;
  tot += parseInt(result);
  console.log(result);

  var e = document.getElementById("q8");
  var result = e.options[e.selectedIndex].value;
  tot += parseInt(result);
  console.log(result);

  var e = document.getElementById("q9");
  var result = e.options[e.selectedIndex].value;
  tot += parseInt(result);
  console.log(result);

  fetch("/reaction/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(tot)
  });

  document.getElementById("finalize").style.display = "none";
  document.getElementById("results").style.display = "block";
  document.getElementById("results").style.float = "center";
};
