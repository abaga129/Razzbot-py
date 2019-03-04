#####################################
# example.py
# Written By Ethan Reker 2017
#####################################

import RPi.GPIO as GPIO
import time
import config
import HCSR04
import L298N
#import logic


def turn():
  stopCount = 0
  print "TURN"
  motor_ctrl.setMode("LEFT")
  time.sleep(.6)
  motor_ctrl.setMode("BACKWARD")
  time.sleep(.3)
  motor_ctrl.setMode("STOP")

stopCount = 0

config.initialize()

sensorFront = HCSR04.HCSR04(config.TRIG1, config.ECHO, "FRONT")
#sensorRight = HCSR04.HCSR04(config.TRIG2, config.ECHO, "RIGHT")
#sensorLeft = HCSR04.HCSR04(config.TRIG4, config.ECHO, "LEFT") 

sensorFront.start()
#sensorRight.start()
#sensorLeft.start()

motor_ctrl = L298N.L298N(22, 11, 12, 13)
motor_ctrl.start()

#logicUnit = logic.LogicalUnit(motor_ctrl, [sensorFront, sensorRight, sensorLeft])

print "Setup Complete"        

#logicUnit.start()

while True:
  print "Front ", sensorFront.read()
  #print "Left ", sensorLeft.read()
  #print "Right ", sensorRight.read()
  time.sleep(0.5)
