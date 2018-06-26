// Sunfounder Raindrop sensor

// lowest and highest sensor readings
const int SENSOR_MIN = 0;
const int SENSOR_MAX = 1024;

void rain_run()
{
  int sensor_reading = analogRead(RAINPIN);
  int range = map(sensor_reading, SENSOR_MIN, SENSOR_MAX, 0, 3);

  switch (range)
  {
  case 0: // Sensor getting wet
    Serial.println("Flood");
    break;
  case 1: // Sensor getting wet
    Serial.println("Rain Warning");
    break;
  case 2: // Sensor dry
    Serial.println("Not Raining");
    break;
  }
  
  Serial.println(sensor_reading);
}
