#####################################
# example.py
# Written By Ethan Reker 2017
#####################################

import RPi.GPIO as GPIO
import time
import config
import HCSR04
import L298N

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

sensor1 = HCSR04.HCSR04(16, 18, "FRONT")

sensor1.start()

motor_ctrl = L298N.L298N(22, 11, 12, 13)
motor_ctrl.start()

while True:
	print "FRONT: ", sensor1.read()
	distance = sensor1.read()
        time.sleep(0.05)
        if distance < 40:
            stopCount = stopCount + 1
            print "STOP"
            motor_ctrl.setMode("STOP")
#            if distance == 0:
#                continue
            if stopCount > 2:
              turn()
              stopCount = 0
            time.sleep(2)
        else:
            print "FORWARD"
            motor_ctrl.setMode("FORWARD")
        
        
