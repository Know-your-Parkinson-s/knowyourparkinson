navigator.permissions.query({ name: "accelerometer" }).then(function(result) {
  if (result.state === "granted") {
    console.log("granted");
    let sensor = new Accelerometer();

    permissions = ["sensors", "accelerometer"];

    sensor.start();

    xval = document.getElementById("xval");
    yval = document.getElementById("yval");
    zval = document.getElementById("zval");

    sensor.onreading = () => {
      console.log("Acceleration along X-axis: " + sensor.x);
      console.log("Acceleration along Y-axis: " + sensor.y);
      console.log("Acceleration along Z-axis: " + sensor.z);
      xval.innerHTML = sensor.x;
      yval.innerHTML = sensor.y;
      zval.innerHTML = sensor.z;
    };

    sensor.onerror = event =>
      console.log(event.error.name, event.error.message);
  } else if (result.state === "prompt") {
    console.log("prompt");
  }
  console.log("Denied");
});

const sensor = new AbsoluteOrientationSensor();
Promise.all([
  navigator.permissions.query({ name: "accelerometer" }),
  navigator.permissions.query({ name: "magnetometer" }),
  navigator.permissions.query({ name: "gyroscope" })
]).then(results => {
  if (results.every(result => result.state === "granted")) {
    sensor.start();
  } else {
    console.log("No permissions to use AbsoluteOrientationSensor.");
  }
});
