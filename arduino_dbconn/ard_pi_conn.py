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
temperature = pieces[4]

# Logs sensor readings to sensor_test.log
def log():
    logging.debug('Humidity: {}'    .format(humidity))
    logging.debug('Wetness: {}'     .format(wetness)) 
    logging.debug('Wind Speed: {} ' .format(wind_speed))
    logging.debug('Pressure: {}'    .format(pressure)) 
    logging.debug('Temperature: {}' .format(temperature))

# Inserts data into MySQL database
def db_insert(config):
    try:
        cnx = mysql.connector.connect(**config)
    # Catches any errors
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Something is wrong with your user name or password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    # Inserts the data
    else:
        cur = cnx.cursor()
        sensor_data = {
                'humidity': humidity,
                'wetness': wetness,
                'wind_speed': wind_speed,
                'temperature': temperature,
                'pressure': pressure
                }
        sensor_add = (
                "INSERT INTO weather_data_test"
                "(humidity,wetness,wind_speed,temperature,pressure)"
                "VALUES (%(humidity)s,%(wetness)s,%(wind_speed)s,%(temperature)s,%(pressure)s)"
                )
        cur.execute(sensor_add,sensor_data)
        cnx.commit()
    # Closes the connection
    finally:
        if cur:
            cur.close()
        if cnx:
            cnx.close()

if __name__ == '__main__':
    # uncomment for logging
    # log()
    database_config = {
        'user': 'root',
        'password': 'test_pass',
        'host': 'localhost',
        'database': 'arduino_pi_weather_station_dev'
        }
    db_insert(database_config)
