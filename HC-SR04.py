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
    while True:
      
      
      
  #Do not call this until conf.initialize() has been called in main program.
  def read(self):
    conf.thread_lock.accquire()
    ret = distance
    conf.thread_lock.release()
    return ret
    
  
  
