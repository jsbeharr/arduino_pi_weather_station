// Adafruit Wind Anemometer

//Setup Variables
int sensor_value = 0; //Variable stores the value direct from the analog pin
float sensor_voltage = 0; //Variable that stores the voltage (in Volts) from the anemometer being sent to the analog pin
float wind_speed = 0; // Wind speed in meters per second (m/s)

//Anemometer Technical Variables
const float VOLTAGE_MIN = .4; // Mininum output voltage from anemometer in mV.
const float VOLTAGE_MAX = 2.0; // Maximum output voltage from anemometer in mV.
const float WIND_SPEED_MAX = 32; // Wind speed in meters/sec corresponding to maximum voltage

float mapFloat(float x, float in_min, float in_max, float out_min, float out_max) {
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

void wind_run()
{
  sensor_value = analogRead(WINDPIN); //Get a value between 0 and 1023 from the analog pin connected to the anemometer

  sensor_voltage = mapFloat(sensor_value, 0, 1023, 0, 5);

  //Convert voltage value to wind speed using range of max and min voltages and wind speed for the anemometer
  if (sensor_voltage <= VOLTAGE_MIN) {
    wind_speed = 0; //Check if voltage is below minimum value. If so, set wind speed to zero.
  } else {
    wind_speed = (sensor_voltage - VOLTAGE_MIN) * WIND_SPEED_MAX / (VOLTAGE_MAX - VOLTAGE_MIN); //For voltages above minimum value, use the linear relationship to calculate wind speed.
  }

  //Print voltage and wind_speed to serial
  Serial.print("Voltage: ");
  Serial.print(sensor_voltage);
  Serial.print("\t");
  Serial.print("Wind speed: ");
  Serial.println(wind_speed);

}
