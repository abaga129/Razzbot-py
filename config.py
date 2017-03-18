################################################################
# THIS FILE MUST BE CONFIGURED BEFORE USING ANY OF THE MODULES #
# Below are variables which indicate which pins on the PI will #
# be used.                                                     #
# - Replace "" with actual pin # without quotes.
################################################################

import RPi.GPIO as GPIO

mode = "BOARD" #define the pin numbering system to be used. (BOARD, BCM)
warnings = "OFF" #change to "ON" to enable warnings

# L298N Pins
A_FORWARD = 7
A_REVERSE = 11
B_FORWARD = 12
B_REVERSE = 13

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
      print "Pin ", pinNo, " set as "
      if mode:
        print "Input"
        GPIO.setup(pinNo, GPIO.IN)
      else:
        print "Output"
        GPIO.setup(pinNo, GPIO.OUT)
    except:
      print "Error setting up pin ", pinNo
      
if mode == "BOARD":
  print "Using BOARD numbering system."
  GPIO.setmode(GPIO.BOARD)
else:
  print "Using BCM numbering system."
  GPIO.setmode(GPIO.BCM) 

if warnings == "OFF":
  print "Warnings OFF."
  GPIO.setwarnings(False)

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
