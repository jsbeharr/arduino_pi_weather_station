# Arduino PI Weather Station
This repo contains code for a weather station built with raspberry pi and arduino.

### Sensors
* [MPL3115A2 Pressure, Humidty, Temperature sensor](https://www.adafruit.com/product/1893)
* [Sun founder rain drop sensor](https://www.aliexpress.com/item/SunFounder-Smart-Electronics-DIY-Raindrop-Sensor-Module-Analyser-for-Arduino-and-Raspberry-Pi/32679787645.html)
* [Anemometer Wind Speed Sensor w/Analog Volt](https://www.adafruit.com/product/1733)
* [DHT11 Temperature and Humidity Sensor Module](https://www.adafruit.com/product/386)

### Arduino Circuit Design
![Arduino Circuit](https://gitlab.eecs.umich.edu/rubinz/arduino_pi_weather_station/raw/master/img_assets/arduino_weather_sensors_v6_bb.png "arduino circuit image")

### Python Setup
It is recommended to use a python virtual environment to keep modules isolated

To install all the python modules run the following command
```shell
pip install -r requirements.txt
```
This will install all the modules and their corresponding version types