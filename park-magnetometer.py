# Simple demo of of the LSM303 accelerometer & magnetometer library.
# Will print the accelerometer & magnetometer X, Y, Z axis values every half
# second.
# Author: Tony DiCola, Stae Plug-in and threshold added by Crystal Penalosa
# License: Public Domain
import time
import RPi.GPIO as GPIO
import os
import json
import geojson
import time
import threading
import urllib
import urllib2
import requests
import Adafruit_LSM303

lsm303 = Adafruit_LSM303.LSM303()

# LED Indicator on GPIO 26
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT)

# Alternatively you can specify the I2C bus with a bus parameter:
#lsm303 = Adafruit_LSM303.LSM303(busum=2)

print('Starting up the Parking Sensors, press Ctrl-C to quit...')
while True:
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_z, mag_y = mag
    print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(
          accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))
    # Wait 5 seconds and repeat.
    if mag_z > -130: 
        GPIO.output(26,GPIO.LOW) 
        status = 'open'
    else: 
        GPIO.output(26,GPIO.HIGH) 
        status = 'closed'

    #Stae Initialize POST
    id = 'pkst2'
    stallNumber = '7'
    parkingStructure = 'Samsung NEXT Parking Garage'
    type = 'compact'
    location = geojson.Point((-73.99048715829849,40.744050339871116))
    url = 'https://municipal.systems/v1/data?key=5802877b-5901-45c0-9ca2-d4301bc7301f'
    payload = {'status':status, 'stallNumber':stallNumber, 'parkingStructure':parkingStructure, 'type':type, 'location':location, 'id':id}
    r = requests.post(url, json=payload) 
        # params='response=false'
    print r.content
    time.sleep(10)
    
