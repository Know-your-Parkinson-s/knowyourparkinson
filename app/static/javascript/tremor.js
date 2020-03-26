// navigator.permissions.query({ name: "accelerometer" }).then(function(result) {
//   if (result.state === "granted") {
//     console.log("granted");
//     let sensor = new Accelerometer();

//     permissions = ["sensors", "accelerometer"];

//     sensor.start();

//     xval = document.getElementById("xval");
//     yval = document.getElementById("yval");
//     zval = document.getElementById("zval");

//     sensor.onreading = () => {
//       console.log("Acceleration along X-axis: " + sensor.x);
//       console.log("Acceleration along Y-axis: " + sensor.y);
//       console.log("Acceleration along Z-axis: " + sensor.z);
//       xval.innerHTML = sensor.x;
//       yval.innerHTML = sensor.y;
//       zval.innerHTML = sensor.z;
//     };

//     sensor.onerror = event =>
//       console.log(event.error.name, event.error.message);
//   } else if (result.state === "prompt") {
//     console.log("prompt");
//   }
//   console.log("Denied");
// });

navigator.permissions.query({ name: "accelerometer" }).then(result => {
  if (result.state === "denied") {
    console.log("Permission to use accelerometer sensor is denied.");
    return;
  }
  // Use the sensor.
});
