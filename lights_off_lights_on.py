#!/usr/bin/env python

import time
from grovepi import *

# variables to store which ports the lights/button are plugged into
led_blue = 2
led_red = 3
led_green = 4
button = 8

pinMode(led_blue, "OUTPUT")
pinMode(led_red, "OUTPUT")
pinMode(led_green, "OUTPUT")

pinMode(button, "INPUT")

while True:
    try:
        isOn = digitalRead(button)
        digitalWrite(led_blue, isOn)
        digitalWrite(led_red, isOn)
        digitalWrite(led_green, isOn)
        time.sleep(.05)

    except KeyboardInterrupt:	# Turn LED off before stopping
        digitalWrite(led_blue, 0)
        digitalWrite(led_red, 0)
        digitalWrite(led_green, 0)
        break

    except IOError:
        print ("Error")
