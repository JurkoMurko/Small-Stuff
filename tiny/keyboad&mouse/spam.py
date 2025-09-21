from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from pynput import keyboard
import time

keyboard = KeyboardController()
mouse = MouseController()

def typing(whatuwanttotype):
    for char in str(whatuwanttotype):
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.1)


def gravity(force):
    time.sleep(2)

    i = 0
    while i < 4000:
        mouse.move(-1, 1)
        i += 1
        time.sleep(force)


def spam(x, y, how_many):
    mouse.position = (x, y)
    mouse.click(Button.left, 1)

    i = 0
    while i < int(how_many):
        keyboard.type("lol :)")
        keyboard.press(Key.enter)
        i += 1
        time.sleep(0.5)


def hotkey():
    # The key combination to check
    COMBINATIONS = [
        {keyboard.Key.shift, keyboard.KeyCode(char='a')},
        {keyboard.Key.shift, keyboard.KeyCode(char='A')}
    ]

    # The currently active modifiers
    current = set()


    def execute():
        print ("Do Something")


    def on_press(key):
        if any([key in COMBO for COMBO in COMBINATIONS]):
            current.add(key)
            if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
                execute()


    def on_release(key):
        if any([key in COMBO for COMBO in COMBINATIONS]):
            current.remove(key)


    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


def cobble():
    while True:
        mouse.press(Button.left)

        if keyboard.shift_pressed:
            break


'''
time.sleep(2)

while True:
    print(mouse.position)
    time.sleep(0.5)
'''
'''
#keyboard.press("a")
#keyboard.release("a")

#keyboard.press(Key.cmd)
#keyboard.release(Key.cmd)

#keyboard.type("Hehehehe! Just imagine how much this is going to suck for you.")


for char in "Hehehehe! Just imagine how much this is going to suck for you.":
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.1)
'''


'''
print(mouse.position)

mouse.position = (10, 20)

mouse.move(20, -13)

# Click the left button
mouse.click(Button.left, 1)
# Click the right button
mouse.click(Button.right, 1)
# Click the middle button
mouse.click(Button.middle, 1)
# Double click the left button
mouse.click(Button.left, 2)
# Click the left button ten times
mouse.click(Button.left, 10)

mouse.press(Button.left)
mouse.release(Button.left)

# Scroll up two steps
mouse.scroll(0, 2)
# Scroll right five steps
mouse.scroll(5, 0)

# This is the bottom right of the page (1535, 863)
'''

'''
from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
'''


# spam(100, 100, 21)

time.sleep(3)
cobble()
