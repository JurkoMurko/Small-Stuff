import RPi.GPIO as GPIO, time
import sys

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(32, 4000)

def SpinMotor(dire):
    p.ChangeFrequency(4000)
    GPIO.output(18,dire)
    p.start(1)
    #GPIO.output(32, False)
    #GPIO.output(32, True)
    time.sleep(0.0016)
    return True
while True:
    dir_input = raw_input("Enter your dir: ") 
    if dir_input == "F":
        print("direction")
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

