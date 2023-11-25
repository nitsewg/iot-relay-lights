# Connect GPIO18 to positive on the IoT relay, connect ground from Pi to ground on relay.

import random
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

#Set relay to "off"
GPIO.output(18,GPIO.LOW)