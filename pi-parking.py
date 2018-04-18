#borrowed from https://github.com/efatsi/Pi-Parking

from SimpleCV import *
import sys
import requests
import json
import geojson
import time
from datetime import datetime

cam = Camera()

image = cam.getImage()
fileName = "screenshot_" + datetime.now().strftime("%m-%d_%H:%M") + ".png"

image.save(fileName)

# crop with full car & no back wall:
image = image.crop(170, 170, 230, 300)

# used to use 100, 400 (was the worst)
# followed by 50, 200 which was terrible
# used 50, 400 with success
# used 25, 400 with success
# used 300, 400 with success
image = image.edges(25, 400)

# make MASK!
mask = Image(image.size())
dl = DrawingLayer(image.size())
# get rid of bushes
dl.polygon([(230, 100), (230, 300), (0, 300), (0, 200)], filled=True, color=Color.WHITE)
# get rid of brick wall
dl.polygon([(0, 0), (50, 0), (15, 300), (0, 300)], filled=True, color=Color.WHITE)
# get rid of back of car
#dl.polygon([(115, 0), (230, 0), (230, 300), (115, 300)], filled=True, color=Color.WHITE)
mask.addDrawingLayer(dl)
mask = mask.applyLayers()

image = image - mask

#image.show()
#raw_input()

image_matrix = image.getNumpy().flatten()

image_pixel_count = cv2.countNonZero(image_matrix)

#print "Image " + fileName + " has " + str(image_pixel_count) + " pixels"

image.save("canny-" + fileName)

if image_pixel_count > 2000:
  print "TAKEN"
  status = {'update[status]': 'taken', 'update[pixel_count]': image_pixel_count}
else:
  print "AVAILABLE"
  status = {'update[status]': 'available', 'update[pixel_count]': image_pixel_count}

# location = geojson.Point((-87.68051147460938,42.04820514755174))
# url = 'https://municipal.systems/v1/data?key=keyData'
# files = {'update[image]': (fileName, open(fileName, 'rb')), 'update[canny_image]': ("canny-" + fileName, open("canny-" + fileName, 'rb'))}
# payload = {'id':id, 'status':status, params='response=false'}
# r = requests.post(url, json=payload)
# print r.status_code
# time.sleep(10)

