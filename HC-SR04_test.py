#####################################
# HC-SR04_test.py
# Written By Ethan Reker 2017
#####################################

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
print "Using BOARD numbering system for GPIO pins."

TRIG = raw_input("Enter Pin Number that is connected to TRIG: ")
ECHO = raw_input("Enter Pin Number that is connected to ECHO: ")

TRIG = int(TRIG)
ECHO = int(ECHO)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

cont = ""
while cont!="n":
  GPIO.output(TRIG, GPIO.LOW)
  time.sleep(2)
  
  GPIO.output(TRIG, GPIO.HIGH)
  time.sleep(0.0001)
  GPIO.output(TRIG, GPIO.LOW)
  
  print "Waiting for rising edge."
  GPIO.wait_for_edge(ECHO, GPIO.RISING)
  start_time = time.time()

  GPIO.wait_for_edge(ECHO, GPIO.FALLING)
  end_time = time.time()
  
  total_time = end_time - start_time
  distance = total_time * 17150
  distance = round(distance, 2)
  print "Distance: ", distance, "cm"
  
  cont = raw_input("Continue?(y/n): ")
    
GPIO.cleanup()
print "Test Complete."
