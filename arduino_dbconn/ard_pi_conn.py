import serial
import time
import logging

# Sets up a logger
logging.basicConfig(
        filename='sensor_test.log',
        level=logging.DEBUG,
        format='%(asctime)s:%(levelname)s:%(message)s')

# Specifies which serial port to listen on
arduino = serial.Serial('/dev/ttyACM0', 9600)

# Reads in data from arduino
data = arduino.readline()
time.sleep(1)
data = arduino.readline()

# Get each piece seperate by a tab
pieces = data.split('\t')

# sets a variable to each sensor reading
humidity    = pieces[0]
wetness     = pieces[1] 
wind_speed  = pieces[2]
pressure    = pieces[3]
temperture  = pieces[4]

# Logs sensor readings to sensor_test.log
logging.debug('Humidity: {}'    .format(humidity))
logging.debug('Wetness: {}'     .format(wetness)) 
logging.debug('Wind Speed: {} ' .format(wind_speed))
logging.debug('Pressure: {}'    .format(pressure)) 
logging.debug('Temperature: {}' .format(temperture))
