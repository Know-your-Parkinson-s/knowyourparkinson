let sensor = new Accelerometer();

permissions = ["sensors"];

var requesting = browser.permissions.request(
  permissions // Permissions object
);

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

sensor.onerror = event => console.log(event.error.name, event.error.message);
