import serial
import mysql.connector
import time

arduino = serial.Serial('/dev/ttyACMO')
arduino.baudrate = 9600

data = arduino.read_all()

pieces = data.split('\t')

humidity = pieces[0]
wetness = pieces[1]
wind_speed = pieces[2]
temperature = pieces[3]
pressure = pieces[4]

print(pieces)


