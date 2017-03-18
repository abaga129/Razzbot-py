################################################################
# THIS FILE MUST BE CONFIGURED BEFORE USING ANY OF THE MODULES #
# Below are variables which indicate which pins on the PI will #
# be used.                                                     #
################################################################

import RPi.GPIO as GPIO

# L298N Pins
A_FORWARD = ""
A_REVERSE = ""
B_FORWARD = ""
B_REVERSE = ""

# HC_SR04 Pins
TRIG1 = ""
TRIG2 = ""
TRIG3 = ""
TRIG4 = ""
TRIG5 = ""
ECHO = ""

# SG90 Pins
SERVO1 = ""
SERVO2 = ""
SERVO3 = ""

def setup_pin(pinNo, mode):
  if pinNo != "":
    try:
      if mode:
        GPIO.setup(pinNo, GPIO.IN)
    except:
      print "Error setting up pin ", pinNo
    
