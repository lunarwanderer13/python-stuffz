import pyautogui as pag

# Setting up failsafe
pag.FAILSAFE = True

def i(size, duration):
    seg = size * (1 / 8)

    pag.dragRel(seg * 4, 0, duration=duration, button='left')
    pag.dragRel(0, -size, duration=duration, button='left')
    pag.dragRel(-seg * 4, 0, duration=duration, button='left')
    pag.dragRel(size, 0, duration=duration, button='left')
    pag.dragRel(-seg * 4, 0, duration=duration, button='left')
    pag.dragRel(0, size, duration=duration, button='left')
    pag.dragRel(seg * 4, 0, duration=duration, button='left')

    pag.moveRel(seg, 0, duration=duration)