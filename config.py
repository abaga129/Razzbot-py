################################################################
# THIS FILE MUST BE CONFIGURED BEFORE USING ANY OF THE MODULES #
# Below are variables which indicate which pins on the PI will #
# be used.                                                     #
# - Replace "" with actual pin # without quotes.
################################################################

import RPi.GPIO as GPIO

mode = "BOARD" #define the pin numbering system to be used. (BOARD, BCM)

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
      else:
        GPIO.setup(pinNo, GPIO.OUT)
    except:
      print "Error setting up pin ", pinNo
      
if mode == "BOARD":
  GPIO.setmode(GPIO.BOARD)
else:
  GPIO.setmode(GPIO.BCM) 

setup_pin(A_FORWARD, 0)
setup_pin(A_REVERSE, 0)
setup_pin(B_FORWARD, 0)
setup_pin(B_REVERSE, 0)
setup_pin(TRIG1, 0)
setup_pin(TRIG2, 0)
setup_pin(TRIG3, 0)
setup_pin(TRIG4, 0)
setup_pin(TRIG5, 0)
setup_pin(SERVO1, 0)
setup_pin(SERVO2, 0)
setup_pin(SERVO3, 0)