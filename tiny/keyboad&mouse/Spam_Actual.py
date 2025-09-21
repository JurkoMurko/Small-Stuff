from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from pynput import keyboard
import time

keyboard = KeyboardController()
mouse = MouseController()


def actual(x, y):
    mouse.position = (x, y)
    mouse.click(Button.left, 1)

    i = 0
    while i < 20:
        keyboard.type("lol :)")
        keyboard.press(Key.enter)
        i += 1
        time.sleep(0.5)


actual(100, 100)
