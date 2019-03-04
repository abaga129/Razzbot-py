import RPi.GPIO as GPIO
import time
import L298N
import random
from collections import deque

GPIO.setmode(GPIO.BOARD)

SENSOR_FRONT_TRIG = 37
SENSOR_FRONT_ECHO = 38
SENSOR_LEFT_TRIG = 35
SENSOR_LEFT_ECHO = 36
SENSOR_RIGHT_TRIG = 31
SENSOR_RIGHT_ECHO = 32

STOP_DISTANCE = 25
random.seed()

TIME_FULL_TURN = 2.7 #seconds

left_average = deque([])
right_average = deque([])
front_average = deque([])

def pivot_left():
    print "Pivoting left"
    motor_ctrl.setMode("BACKWARD")
    time.sleep(1)
    motor_ctrl.setMode("RIGHT")
    time.sleep(TIME_FULL_TURN / 4)
    motor_ctrl.setMode("STOP")

def pivot_right():
    print "Pivoting right"
    motor_ctrl.setMode("BACKWARD")
    time.sleep(1)
    motor_ctrl.setMode("LEFT")
    time.sleep(TIME_FULL_TURN / 4)
    motor_ctrl.setMode("STOP")

def full_turn():
    motor_ctrl.setMode("RIGHT")
    time.sleep(TIME_FULL_TURN)
    motor_ctrl.setMode("STOP")

def forward():
    motor_ctrl.setMode("FORWARD")

def get_average(list):
    if len(list) > 0 :
        result = list[0]
        for i in range(0, len(list)):
            result += list[i] / 2
    else:
        result = 0
    return result
        

def wander():
    global left_average
    global right_average
    global front_average

    prev_left = left_average
    
    
    front_sensor.read()
    time.sleep(0.010)
    left_sensor.read()
    time.sleep(0.010)
    right_sensor.read()
    time.sleep(0.010)

    #if(left_sensor.current_reading < 200):
    left_average.append(left_sensor.current_reading)
    if(len(left_average) > 10):
        left_average.popleft()
#if(right_sensor.current_reading < 200):
    right_average.append(right_sensor.current_reading)
    if(len(right_average) > 10):
        right_average.popleft()
#if(front_sensor.current_reading < 200):
    front_average.append(front_sensor.current_reading)
    if(len(front_average) > 10):
        front_average.popleft()

    print "Averages: " + str(left_average) + " : " + str(right_average) + " : " + str(front_average) + "\n"
    
    print("Front " + str(front_sensor.current_reading))
    print("Left " + str(left_sensor.current_reading))
    print("Right " + str(right_sensor.current_reading))
    if min([front_sensor.current_reading, left_sensor.current_reading, right_sensor.current_reading]) > STOP_DISTANCE:
        forward()
        left = get_average(left_average)
        right = get_average(right_average)
        front = get_average(front_average)

        #debug
        print "\n\nAverages " + str(left) + " : " + str(right) + " : " + str(front) + "\n"
        #time.sleep(1)
        
        if abs(left - left_sensor.current_reading) < 2 or abs(right - right_sensor.current_reading) < 2 or abs(front - front_sensor.current_reading) < 2 :
            full_turn()
            
    else:
        if left_sensor.current_reading < STOP_DISTANCE and left_sensor.current_reading < right_sensor.current_reading:
            pivot_right()
            time.sleep(3)
        elif right_sensor.current_reading < STOP_DISTANCE and right_sensor.current_reading < left_sensor.current_reading:
            pivot_left()
            time.sleep(3)
        else:
            pivot_left()
            pivot_left()

    

class HCSR04:
    def __init__(self, trig_pin, echo_pin):
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        GPIO.setup(self.trig_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def read(self):
        GPIO.output(self.trig_pin, GPIO.HIGH)
        time.sleep(0.0001)
        GPIO.output(self.trig_pin, GPIO.LOW)

        GPIO.wait_for_edge(self.echo_pin, GPIO.BOTH, timeout = 1000)
        start_time = time.time()
        GPIO.wait_for_edge(self.echo_pin, GPIO.BOTH, timeout = 1000)
        end_time = time.time()

        total_time = end_time - start_time
        distance = total_time * 17150
        distance = round(distance, 2)

        self.current_reading = distance

    def cleanup(self):
        GPIO.cleanup(self.trig_pin)
        GPIO.cleanup(self.echo_pin)

motor_ctrl = L298N.L298N(22, 11, 12, 13)
motor_ctrl.setMode("STOP")
motor_ctrl.start()
        
front_sensor = HCSR04(SENSOR_FRONT_TRIG, SENSOR_FRONT_ECHO)
left_sensor = HCSR04(SENSOR_LEFT_TRIG, SENSOR_LEFT_ECHO)
right_sensor = HCSR04(SENSOR_RIGHT_TRIG, SENSOR_RIGHT_ECHO)

while True:
    #decision = random.rand_int(0,2)
    wander()


