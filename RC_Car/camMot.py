import time
import os
import logging
import RPi.GPIO as GPIO

from time import sleep
import RPi.GPIO as GPIO


def SetAngle(angle):
    duty = angle / 18 + 2.5
    GPIO.output(12, True)
    pwm.ChangeDutyCycle(duty)
    #sleep(1)
    #GPIO.output(12, False)
    #pwm.ChangeDutyCycle(0)

 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 50)
pwm.start(0)

while True: 
	dir_input = raw_input("Enter angle:")
        if dir_input == "stop":
            pwm.stop();
        else:
            SetAngle(int(dir_input))
        
        

