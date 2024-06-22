# Libraries
import pyautogui as pag
import time
import math

# Setting up failsafe
pag.FAILSAFE = True

def triangle(size, duration):
    height = (size * math.sqrt(3)) / 2
    drag = size / 2

    time.sleep(5)

    pag.moveRel(0, -height/2)

    pag.dragRel(drag, height, duration=duration, button='left')
    pag.dragRel(-size, 0, duration=duration, button='left')
    pag.dragRel(drag, -height, duration=duration, button='left')