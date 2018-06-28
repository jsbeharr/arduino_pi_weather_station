// DHT 11 Temperature & Humidity Sensor

// Depends on the following Arduino libraries:
// - Adafruit Unified Sensor Library: https://github.com/adafruit/Adafruit_Sensor
// - DHT Sensor Library: https://github.com/adafruit/DHT-sensor-library

#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>

#define DHTTYPE DHT11

// enable DHT11 sensor from the set pin
DHT_Unified dht(DHTPIN, DHTTYPE);

void dht_humidity_temp_setup()
{
  // Initialize device.
  dht.begin();
}

void dht_humidity_temp_run() {
  sensors_event_t event;  
  // Get humidity event and print its value.
  dht.humidity().getEvent(&event);
  if (isnan(event.relative_humidity)) {
    Serial.println("Error reading humidity!");
  }
  else {
    Serial.print(event.relative_humidity);
  }
}
