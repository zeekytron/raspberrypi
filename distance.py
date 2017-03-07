#!/usr/bin/env python

import time
import grovepi
from grove_rgb_lcd import *

# using the Grove board, distance sensor, and LCD display, show the distance of objects
# that are in front of the sensor

# Connect the Grove Ultrasonic Ranger to digital port D7
# SIG,NC,VCC,GND
ultrasonic_ranger = 7

distance = 0

while True:
    try:
        # Read distance value from Ultrasonic
        newDistance = grovepi.ultrasonicRead(ultrasonic_ranger)
        if (distance != newDistance):
            distance = newDistance
            setText("distance: %s" % distance)
            setRGB(0, 128, 64)

    except TypeError:
        print ("Error")
    except IOError:
        print ("Error")
