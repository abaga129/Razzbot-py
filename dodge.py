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

STOP_DISTANCE = 40

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

sensorC = HCSR04.HCSR04(37, 38, "FRONT")
sensorC.start()
sensorL = HCSR04.HCSR04(35, 36, "LEFT")
sensorL.start()
sensorR = HCSR04.HCSR04(31, 32, "RIGHT")
sensorR.start()

motor_ctrl = L298N.L298N(22, 11, 12, 13)
motor_ctrl.start()
motor_ctrl.setMode("FORWARD")

def checkDistances():
  print "Checking distances"
  center = sensorC.read()
  left = sensorL.read()
  right = sensorR.read()
  print "Center " + str(center) + " Left " + str(left) + " Right " + str(right)
  # return  center < STOP_DISTANCE or left < STOP_DISTANCE or right < STOP_DISTANCE
  return center

try:
  while True:
    distanceCheck = checkDistances()
    if distanceCheck < 40:
      print "STOPPING"
      motor_ctrl.setMode("STOP")
      time.sleep(0.1)
      turn()
    else:
      print "FORWARD"
      motor_ctrl.setMode("FORWARD")
      time.sleep(0.1)
except KeyboardInterrupt:
  motor_ctrl._stop()
  sensor1._stop()
  sys.exit()
  
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

        
        
