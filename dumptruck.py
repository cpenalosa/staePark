# Simple demo of of the LSM303 accelerometer & magnetometer library.
# Will print the accelerometer & magnetometer X, Y, Z axis values every half
# second.
# Author: Tony DiCola, Stae Plug-in and threshold added by Crystal Penalosa
# License: Public Domain
import time
from time import gmtime, strftime
from Adafruit_LED_Backpack import AlphaNum4
import RPi.GPIO as GPIO
import os
import json
import geojson
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


# Create display instance on default I2C address (0x70) and bus number.
display = AlphaNum4.AlphaNum4()

# Initialize the display. Must be called once before using the display.
display.begin()

# Scroll a message across the display

print('Press Ctrl-C to quit.')
while True:
    # Clear the display buffer.
    display.clear()
    # Print a 4 character string to the display buffer.
    display.print_str(message[pos:pos+4])
    # Write the display buffer to the hardware.  This must be called to
    # update the actual display LEDs.
    display.write_display()
    # Increment position. Wrap back to 0 when the end is reached.
    pos += 1
    if pos > len(message)-4:
        pos = 0
    # Delay for half a second.
    time.sleep(0.2)

# Note that the alphanumeric display has the same number printing functions
# as the 7 segment display.  See the sevensegment_test.py example for good
# examples of these functions.



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
        available = True
        message = '0001' 
        pos = 0
    else: 
        GPIO.output(26,GPIO.HIGH) 
        available = False
        message = '0000' 
        pos = 0
    display.clear()
    # Print a 4 character string to the display buffer.
    display.print_str(message[pos:pos+4])
    # Write the display buffer to the hardware.  This must be called to
    # update the actual display LEDs.
    display.write_display()
    # Increment position. Wrap back to 0 when the end is reached.

    #Stae Initialize POST
    id = 'DPW dump truck'
    notes = 'Parking Stall 1'
    name = 'Openbox Big Conference Room'
    type = 'DPW Stall'
    location = geojson.Point((-73.991154, 40.742809))
    url = 'https://municipal.systems/v1/data?key=5802877b-5901-45c0-9ca2-d4301bc7301f'
    payload = {'available':available, 'notes':notes, 'name':name, 'type':type, 'location':location, 'id':id}
    r = requests.post(url, json=payload) 
        # params='response=false'
    print r.content
    time.sleep(10)