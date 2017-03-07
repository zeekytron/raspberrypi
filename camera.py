#!/usr/bin/env python

# This script will start the camera preview and then turn it off in 10 seconds
# if you press the button (plugged into port 8 on the Grove board), it will take
# a snapshot and then turn the camera off immediately

from picamera import PiCamera
from time import sleep
from grovepi import *

#which port is the button plugged into?
button = 8
pinMode(button, "INPUT")

camera = PiCamera()

#timer variables
howLongToWait = 10
interval = .05

camera.start_preview()
print "start preview"

counter = 0
while counter < howLongToWait:
    try:
        if (digitalRead(button)):
            camera.capture('/home/pi/Desktop/image1.jpg')
            print "image captured"
            break
        counter = counter + interval
        time.sleep(interval)

    except KeyboardInterrupt:
        break

    except IOError:
        print ("Error")

print "stop preview"
camera.stop_preview()
