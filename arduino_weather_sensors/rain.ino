// Sunfounder Raindrop sensor

// lowest and highest sensor readings
const int SENSOR_MIN = 0;
const int SENSOR_MAX = 1024;

void rain_run()
{
  int sensor_reading = analogRead(RAINPIN);  
  Serial.print(sensor_reading);
}
