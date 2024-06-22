# Libraries
import pyautogui as pag
import time

# Setting up failsafe
pag.FAILSAFE = True

def solid(lenght, duration):
    time.sleep(5)

    pag.dragRel(lenght, 0, duration=duration, button='left')