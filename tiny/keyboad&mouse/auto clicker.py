from pynput.mouse import Button, Controller as MouseController
import time
import keyboard
from random import randint

mouse = MouseController()


def auto(sec, howmany):
    while True:
        if keyboard.is_pressed("s"):
            i = 0
            print(howmany)
            while i < 10000:
                time.sleep(sec + randint(-0.1, 0.1))
                mouse.click(Button.left, 1)
                i += 1
                if keyboard.is_pressed("q"):
                    break


time.sleep(1)
auto(0.005, 1)
