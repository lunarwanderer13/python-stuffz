# Libraries
import pyautogui as pag
import time

# Setting up failsafe
pag.FAILSAFE = True

def spiral(duration):
    num = int(input('How many spirals do you want: '))
    drag = 0

    time.sleep(5)

    for i in range(num):
        pag.dragRel(drag+2.5, 0, duration=duration, button='left')
        pag.dragRel(0, drag+5, duration=duration, button='left')
        pag.dragRel(-drag-7.5, 0, duration=duration, button='left')
        pag.dragRel(0, -drag-10, duration=duration, button='left')

        drag += 10