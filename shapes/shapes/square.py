# Libraries
import pyautogui as pag
import time

# Setting up failsafe
pag.FAILSAFE = True

def square(size, duration):
    drag = size / 2

    time.sleep(5)

    pag.moveRel(-drag, -drag)

    pag.dragRel(size, 0, duration=duration, button='left')
    pag.dragRel(0, size, duration=duration, button='left')
    pag.dragRel(-size, 0, duration=duration, button='left')
    pag.dragRel(0, -size, duration=duration, button='left')