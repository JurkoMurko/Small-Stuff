from pynput.mouse import Button, Controller as MouseController

mouse = MouseController()


def cobble():
    mouse.press(Button.left)

cobble()