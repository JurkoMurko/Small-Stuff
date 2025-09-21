import pyautogui

name = "pic"
extension = ".jpg"

i = 1
while i < 20:
    file_name = f"{name}{i}{extension}"
    try:
        pyautogui.screenshot(r"G:\\My Drive\\juraj@andrews\\Code\\test\\" + file_name)
        break
    except FileExistsError:
        i += 1
