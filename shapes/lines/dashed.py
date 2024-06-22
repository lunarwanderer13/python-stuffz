# Libraries
import pyautogui as pag
import time
import math

# Setting up failsafe
pag.FAILSAFE = True

def dashed(lenght, duration):
    lenght = math.floor(lenght / 2)
    num = int(input('How many segments should the line have: '))
    duration /= num

    time.sleep(5)

    for i in range(num):
        pag.dragRel(lenght / num, 0, duration=duration, button='left')
        pag.moveRel(lenght / num, 0, duration=duration)