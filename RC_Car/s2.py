import RPi.GPIO as GPIO, time
import sys

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

p = GPIO.PWM(13, 4000)

def SpinMotor(dire): 
    p.ChangeFrequency(4000)
    GPIO.output(15,dire)
    p.start(1)
    time.sleep(0.0016)
    return True
while True:
    dir_input = raw_input("Enter your dir: ") 
    if dir_input == "F":
        print("direction--")
        SpinMotor(True)
    elif dir_input == "B":
        SpinMotor(False)
    elif dir_input == "stop":
        p.stop()  
        dir_input = ""  
    elif dir_input == "shutdown":
        p.stop()
        GPIO.cleanup()
        break

