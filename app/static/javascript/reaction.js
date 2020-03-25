var clickedTime;
var createdTime;
var reactionTime;
var testno = 0;
var vals = [];
var state = "INIT";
var container = document.getElementById("reactionContainer");
var tapper = document.getElementById("tapTarget");
var sendbutton = document.getElementById("submitButton");

function changeColor() {
  var time = Math.random();
  time = time * 5000;
  testno = testno + 1;

  setTimeout(function() {
    container.classList.remove("is-success");
    container.classList.add("is-danger");
    createdTime = Date.now();
  }, time);
}

tapper.onclick = function() {
  clickedTime = Date.now();

  if (testno == 0) {
    changeColor();
  } else {
    if (container.classList.contains("is-danger")) {
      if (state == "INIT") {
        reactionTime = clickedTime - createdTime;
        vals.push(reactionTime);

        document.getElementById("printReactionTime").innerHTML =
          "Your Reaction Time is: " + reactionTime + " ms";

        document.getElementById("countTime").innerHTML =
          "Test Count: " + testno;

        container.classList.remove("is-danger");
        container.classList.add("is-success");

        if (testno < 3) {
          changeColor();
        } else {
          state = "DONE";
        }
      }
    }
  }

  if (state == "DONE") {
    sender();
  }
};

function sender() {
  fetch("/reaction/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(vals)
  });
}
