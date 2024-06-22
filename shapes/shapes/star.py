# Libraries
import pyautogui as pag
import time

# Setting up failsafe
pag.FAILSAFE = True

def star(size, duration):
    drag = size / 2

    time.sleep(5)

    pag.moveRel(0, -drag)

    pag.dragRel(size / 2, size, duration=duration, button='left')
    pag.dragRel(-size, -size * .666, duration=duration, button='left')
    pag.dragRel(size, 0, duration=duration, button='left')
    pag.dragRel(-size, size * .666, duration=duration, button='left')
    pag.dragRel(size / 2, -size, duration=duration, button='left')