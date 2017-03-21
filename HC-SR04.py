#########################################################
# HC-SR04.py                                            #
# Written by Ethan Reker 2017                           #
# This module is intended to setup the sensor and       #
# allow simple reading of it.                           #
#########################################################

import threading
import conf

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
             
  def run(self):
    keep = True
    while keep==True:
      GPIO.output(TRIG, GPIO.LOW)
      time.sleep(2)
      
      GPIO.output(TRIG, GPIO.HIGH)
      time.sleep(0.00001)
      GPIO.output(TRIG, GPIO.LOW)
      
      GPIO.wait_for_edge(ECHO, GPIO.RISING)
      start_time = time.time()
      GPIO.wait_for_edge(ECHO, GPIO.FALLING)
      end_time = time.time()
      
      duration = start_time - end_time
      dist = duration * 17150
      conf.thread_lock.acquire()
      distance = dist
      conf.thread_lock.release()
      
  #Do not call this until conf.initialize() has been called in main program.
  def read(self):
    conf.thread_lock.acquire()
    ret = distance
    conf.thread_lock.release()
    return ret
  
  def stop(self):
    keep = False
  
  
