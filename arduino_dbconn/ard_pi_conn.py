import serial
import time
import logging
import mysql.connector
from mysql.connector import errorcode

# Sets up a logger
logging.basicConfig(
        filename='sensor_test.log',
        level=logging.DEBUG,
        format='%(asctime)s:%(levelname)s:%(message)s')

# database config
config = {
        'user': 'root',
        'password': 'test_pass',
        'host': 'localhost',
        'database': 'arduino_pi_weather_station_dev'
        }

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

cnx = cur = None
try:
    cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Something is wrong with your user name or password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cur = cnx.cursor()
    cur.execute('show databases;')
    for row in cur.fetchall():
        print(row)
finally:
    if cur:
        cur.close()
    if cnx:
        cnx.close()
