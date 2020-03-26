var el = document.getElementById("sketchpad");
var pad = new Sketchpad(el);

// setLineColor
function setLineColor(e) {
  var color = e.target.value;
  if (!color.startsWith("#")) {
    color = "#" + color;
  }
  pad.setLineColor(color);
}

// setLineSize
function setLineSize(e) {
  var size = e.target.value;
  pad.setLineSize(size);
}

// undo
function undo() {
  pad.undo();
}
document.getElementById("undo").onclick = undo;

// redo
function redo() {
  pad.redo();
}
document.getElementById("redo").onclick = redo;

// clear
function clear() {
  pad.clear();
}
document.getElementById("clear").onclick = clear;

// resize
window.onresize = function(e) {
  pad.resize(el.offsetWidth);
};
