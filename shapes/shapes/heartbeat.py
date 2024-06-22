# Libraries
import pyautogui as pag
import time
import random

# Setting up failsafe
pag.FAILSAFE = True

def heartbeat(duration):
    lenght = int(input('How long should the heartbeat be: ')) / 5
    maxHeight = int(input('What should be the maximum height: '))

    if maxHeight < 15:
        maxHeight = 15

    height = 0

    time.sleep(5)

    pag.dragRel(lenght, 0, duration=duration, button='left')
    for i in range(5):
        height = random.randint(15, maxHeight)
        pag.dragRel(lenght / 4, -height, duration=duration, button='left')
        pag.dragRel(lenght / 4, height * 2, duration=duration, button='left')
        pag.dragRel(lenght / 4, -height, duration=duration, button='left')
        pag.dragRel(lenght / 4, 0, duration=duration, button='left')
    pag.dragRel(lenght, 0, duration=duration, button='left')