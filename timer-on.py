# Connect GPIO18 to positive on the IoT relay, connect ground from Pi to ground on relay.

import random
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

#Set up random sleep time
randSleep = random.randint(1,1200)
time.sleep(randSleep)

#Set relay to "on"
GPIO.output(18,GPIO.HIGH)