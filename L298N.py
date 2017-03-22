####################################################################
# L298N.py                                                         #
# Created by Ethan Reker 2017                                      #
# Module to simplify using the motor controller from the GPIO on   #
# a raspberry pi                                                   #
####################################################################

import threading
import config as conf
import RPi.GPIO as GPIO
import time

class L298N(threading.Thread):
  A0 = 0
  A1 = 0
  B0 = 0
  B1 = 0
  mode = "STOP"  

  def __init__(self, A0, A1, B0, B1):
    threading.Thread.__init__(self)
    self.A0 = A0
    self.A1 = A1
    self.B0 = B0
    self.B1 = B1
    GPIO.setup(self.A0, GPIO.OUT)
    GPIO.setup(self.A1, GPIO.OUT)
    GPIO.setup(self.B0, GPIO.OUT)
    GPIO.setup(self.B1, GPIO.OUT)

  def run(self):
    while True:
      conf.thread_lock.acquire()	
      mode = self.mode	
      conf.thread_lock.release()

      if mode == "STOP":
        GPIO.output(self.A0, GPIO.LOW)
        GPIO.output(self.A1, GPIO.LOW)
        GPIO.output(self.B0, GPIO.LOW)
        GPIO.output(self.B1, GPIO.LOW)

      if mode == "FORWARD":
        GPIO.output(self.A0, GPIO.HIGH)
        GPIO.output(self.A1, GPIO.LOW)
        GPIO.output(self.B0, GPIO.HIGH)
        GPIO.output(self.B1, GPIO.LOW)

      if mode == "BACKWARD":
        GPIO.output(self.A0, GPIO.LOW)
        GPIO.output(self.A1, GPIO.HIGH)
        GPIO.output(self.B0, GPIO.LOW)
        GPIO.output(self.B1, GPIO.HIGH)

      if mode == "LEFT":
        GPIO.output(self.A0, GPIO.HIGH)
        GPIO.output(self.A1, GPIO.LOW)
        GPIO.output(self.B0, GPIO.LOW)
        GPIO.output(self.B1, GPIO.HIGH)

      if mode == "RIGHT":
        GPIO.output(self.A0, GPIO.LOW)
        GPIO.output(self.A1, GPIO.HIGH)
        GPIO.output(self.B0, GPIO.HIGH)
        GPIO.output(self.B1, GPIO.LOW)
      time.sleep(0.1)

  def setMode(self, mode):
  	conf.thread_lock.acquire()
  	self.mode = mode
  	conf.thread_lock.release()
