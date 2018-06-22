// Sunfounder Raindrop sensor

// lowest and highest sensor readings:
const int sensorMin = 0;    // sensor minimum
const int sensorMax = 1024; // sensor maximum

void rain_run()
{

  int sensorReading = analogRead(RAINPIN);
  int range = map(sensorReading, sensorMin, sensorMax, 0, 3);

  // range value:
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
  Serial.println(sensorReading);
}
