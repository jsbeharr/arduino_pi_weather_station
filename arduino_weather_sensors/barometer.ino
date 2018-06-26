// MPL3115A2 Pressure, Altitude, and Barometer Sensor

#include <Wire.h>
#include <Adafruit_MPL3115A2.h>

// Power by connecting Vin to 3-5V, GND to GND
// Uses I2C - connect SCL to the SCL pin, SDA to SDA pin
// See the Wire tutorial for pinouts for each Arduino
// http://arduino.cc/en/reference/wire
Adafruit_MPL3115A2 baro = Adafruit_MPL3115A2();

void barometer_run() {

  if (! baro.begin()) {
    Serial.println("Couldnt find sensor");
    return;
  }

  float pascals = baro.getPressure();
  Serial.print(pascals / 3377);
  
  Serial.print('\t');

  float tempF = (baro.getTemperature() * (9/5) ) + 32;
  Serial.print(tempF);

}
