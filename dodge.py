#####################################
# example.py
# Written By Ethan Reker 2017
#####################################

import RPi.GPIO as GPIO
import time
import config;
import sys
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

# sensor1 = HCSR04.HCSR04(37, 38, "FRONT")

# sensor1.run()

motor_ctrl = L298N.L298N(22, 11, 12, 13)
motor_ctrl.run()

# try:
#   while True:
# 	distance = sensor1.read()
#   print "FRONT: ", distance
#         time.sleep(0.05)
#         if distance < 40:
#             stopCount = stopCount + 1
#             print "STOP"
#             motor_ctrl.setMode("STOP")
#             if stopCount > 2:
#               turn()
#               stopCount = 0
#             time.sleep(2)
#         else:
#             print "FORWARD"
#             motor_ctrl.setMode("FORWARD")
# except KeyboardInterrupt:
#   print "Exiting program"
#   sys.exit()

        
        
