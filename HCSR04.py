#########################################################
# HC-SR04.py                                            #
# Written by Ethan Reker 2017                           #
# This module is intended to setup the sensor and       #
# allow simple reading of it.                           #
#########################################################

import threading
import config as conf
import RPi.GPIO as GPIO
import time

class HCSR04(threading.Thread):
  TRIG = 0
  ECHO = 0
  name = ""
  distance = 0
  keep = True
  
  def __init__(self, TRIG, ECHO, name):
    threading.Thread.__init__(self)
    self.TRIG = TRIG
    self.ECHO = ECHO
    self.name = name
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)    
         
  def run(self):
    keep = True
    while keep==True:
      GPIO.output(self.TRIG, GPIO.LOW)
      time.sleep(0.1)
      
      GPIO.output(self.TRIG, GPIO.HIGH)
      time.sleep(0.00001)
      GPIO.output(self.TRIG, GPIO.LOW)
      
      #print "Waiting For Edge"
      GPIO.wait_for_edge(self.ECHO, GPIO.RISING, timeout=1000)
      start_time = time.time()
      GPIO.wait_for_edge(self.ECHO, GPIO.FALLING, timeout=2000)
      end_time = time.time()
      
      
      duration = end_time - start_time
      dist = duration * 17150
      #print "Distance ", dist, "Duration ", duration
      if dist > 400 or dist < 3:
        dist = 0
      #print "Waiting for lock"
      conf.thread_lock.acquire()
      self.distance = dist
      conf.thread_lock.release()
      
  #Do not call this until conf.initialize() has been called in main program.
  def read(self):
    #print "Reading"
    conf.thread_lock.acquire()
    ret = self.distance
    conf.thread_lock.release()
    return ret
  
  def stop(self):
    keep = False
  
  
