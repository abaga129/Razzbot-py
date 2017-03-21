#####################################
# HC-SR04_test.py
# Written By Ethan Reker 2017
#####################################

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
print "Using BOARD numbering system for GPIO pins."

TRIG = raw_input("Enter Pin Number that is connected to TRIG: ")
ECHO = raw_input("Enter Pin Number that is connected to ECHO: ")

TRIG = int(TRIG)
ECHO = int(ECHO)
GPIO.cleanup(TRIG)
GPIO.cleanup(ECHO)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

cont = ""
while cont!="n":
  GPIO.output(TRIG, GPIO.LOW)
  time.sleep(1)
  
  GPIO.output(TRIG, GPIO.HIGH)
  time.sleep(0.0001)
  GPIO.output(TRIG, GPIO.LOW)
  
  #print "Waiting for edge."
  GPIO.wait_for_edge(ECHO, GPIO.BOTH, timeout=1000)
  start_time = time.time()

  GPIO.wait_for_edge(ECHO, GPIO.BOTH, timeout=1000)
  end_time = time.time()
  
  total_time = end_time - start_time
  distance = total_time * 17150
  distance = round(distance, 2)
  if distance > 3 and distance < 400: 
    print "Distance: ", distance, "cm"
  else:
    print "Out of Range"  

  cont = raw_input("Continue?(y/n): ")
    
GPIO.cleanup()
print "Test Complete."
