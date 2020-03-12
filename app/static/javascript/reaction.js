// function makeBox() {
//   var time = Math.random();
//   time = time * 3000;

//   setTimeout(function() {
//     document.getElementById("box").style.top = top + "px";
//     document.getElementById("box").style.left = left + "px";
//     document.getElementById("box").style.display = "block";

//     createdTime = Date.now();
//   }, time);
// }

// document.getElementById("box").onclick = function() {
//   clickedTime = Date.now();
//   reactionTime = (clickedTime - createdTime) / 1000;

//   document.getElementById("printReactionTime").innerHTML =
//     "Your Reaction Time is: " + reactionTime + "seconds";

//   this.style.display = "none";

//   makeBox();
// };

var clickedTime;
var createdTime;
var reactionTime;
var testno = 0;

function changeColor() {
  var time = Math.random();
  time = time * 5000;
  testno = testno + 1;

  setTimeout(function() {
    document.getElementById("reactionContainer").classList.remove("is-success");
    document.getElementById("reactionContainer").classList.add("is-danger");
    createdTime = Date.now();
  }, time);
}

document.getElementById("reactionContainer").onclick = function() {
  clickedTime = Date.now();
  reactionTime = (clickedTime - createdTime) / 1000;

  document.getElementById("printReactionTime").innerHTML =
    "Your Reaction Time is: " + reactionTime + "seconds";

  document.getElementById("countTime").innerHTML = "Test Count: " + testno;

  this.classList.remove("is-danger");
  this.classList.add("is-success");
  if (testno < 3) {
    changeColor();
  } else {
    setTimeout(function() {
      document.getElementById("nextTest").click();
    }, 3000);
  }
};

setTimeout(function() {
  changeColor();
}, 1000);
