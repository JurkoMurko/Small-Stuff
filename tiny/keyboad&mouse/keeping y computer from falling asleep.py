from pynput.mouse import Controller as MouseController
import time

mouse = MouseController()

x = 100

while True:
    time.sleep(1)
    mouse.move(x, x)
    x *= -1
