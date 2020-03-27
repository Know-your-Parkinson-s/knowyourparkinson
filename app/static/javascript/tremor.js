var pad = new Sketchpad({
  element: "#sketchpad",
  width: 350,
  height: 350
});

pad.color = "#000";
pad.penSize = 10;

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

document.getElementById("download").onclick = function() {
  document.getElementById("sketchpad").toBlob(function(blob) {
    saveAs(blob, "spiral.jpg");
  });
};
