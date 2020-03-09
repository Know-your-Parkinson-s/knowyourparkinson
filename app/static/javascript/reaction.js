var clickedTime;
var createdTime;
var reactionTime;

function makeBox() {
  var time = Math.random();
  time = time * 3000;

  setTimeout(function() {
    var top = Math.random();
    top = top * 300;
    var left = Math.random();
    left = left * 500;

    document.getElementById("box").style.top = top + "px";
    document.getElementById("box").style.left = left + "px";
    document.getElementById("box").style.display = "block";

    createdTime = Date.now();
  }, time);
}

document.getElementById("box").onclick = function() {
  clickedTime = Date.now();

  reactionTime = (clickedTime - createdTime) / 1000;

  document.getElementById("printReactionTime").innerHTML =
    "Your Reaction Time is: " + reactionTime + "seconds";

  this.style.display = "none";

  makeBox();
};

makeBox();
