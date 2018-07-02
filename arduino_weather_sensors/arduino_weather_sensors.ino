/*
 Name:		arduino_weather_sensors.ino
 Created:	6/22/2018 3:08:51 PM
 Author:	Justin B., Zach R.
*/

#define DHTPIN  2
#define RAINPIN A0
#define WINDPIN A1      

void setup() 
{
  Serial.begin(9600);
  dht_humidity_temp_setup();
}


/*
  Prints the following to serial output
  
  "humidity(%)  wetness(sensor reading)  wind_speed(m/s)  pressure(Inches(Hg))  temperture(F)  
*/

void loop() 
{
  dht_humidity_temp_run();
  Serial.print('\t');
  rain_run();
  Serial.print('\t');
  wind_run();
  Serial.print('\t');
  barometer_run();
  Serial.print('\t');
  Serial.println();
  delay(2000);
}
