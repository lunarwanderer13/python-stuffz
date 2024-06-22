# Libraries
import pyautogui as pag
import time

# Setting up failsafe
pag.FAILSAFE = True

def heart(size, duration):
    drag = size / 3
    seg = size / 6

    time.sleep(5)

    pag.moveRel(0, -drag)

    pag.dragRel(seg, -seg, duration=duration, button='left')
    pag.dragRel(seg, 0, duration=duration, button='left')
    pag.dragRel(seg, seg, duration=duration, button='left')
    pag.dragRel(0, seg, duration=duration, button='left')
    pag.dragRel(-size / 2, size / 2, duration=duration, button='left')
    pag.dragRel(-size / 2, -size / 2, duration=duration, button='left')
    pag.dragRel(0, -seg, duration=duration, button='left')
    pag.dragRel(seg, -seg, duration=duration, button='left')
    pag.dragRel(seg, 0, duration=duration, button='left')
    pag.dragRel(seg, seg, duration=duration, button='left')