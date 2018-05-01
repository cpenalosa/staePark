# Simple demo of of the LSM303 accelerometer & magnetometer library.
# Will print the accelerometer & magnetometer X, Y, Z axis values every half
# second.
# Author: Tony DiCola, Stae Plug-in and threshold added by Crystal Penalosa
# License: Public Domain
import time
import RPi.GPIO as GPIO

# Import the LSM303 module.
import Adafruit_LSM303


# Create a LSM303 instance.
lsm303 = Adafruit_LSM303.LSM303()

# Turn on a LED on GPIO 26
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
    if mag_z > -100: GPIO.output(26,GPIO.HIGH), status = 'open'
    else: GPIO.output(26,GPIO.LOW), status = 'closed'

    #Stae Initialize POST
    id = 'pkst1'
    stallNumber = '10'
    parkingStructure = 'Grand Central Tech Parking Garage'
    type = 'compact'
    location = geojson.Point((-73.97782176733017,40.753421860439836))
    url = 'https://municipal.systems/v1/data?key=5802877b-5901-45c0-9ca2-d4301bc7301f'
    payload = {'status':status, 'stallNumber':stallNumber, 'parkingStructure':parkingStructure, 'type':type, 'location':location, 'id':id}
    r = requests.post(url, json=payload) 
        # params='response=false'
    print = r.content
    time.sleep(10)
    