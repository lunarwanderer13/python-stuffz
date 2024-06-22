import pyautogui as pag

# Setting up failsafe
pag.FAILSAFE = True

def e(size, duration):
    seg = size * (1 / 8)

    pag.dragRel(size, 0, duration=duration, button='left')
    pag.dragRel(-size, 0, duration=duration, button='left')
    pag.dragRel(0, -seg * 4, duration=duration, button='left')
    pag.dragRel(seg * 7, 0, duration=duration, button='left')
    pag.dragRel(-seg * 7, 0, duration=duration, button='left')
    pag.dragRel(0, -seg * 4, duration=duration, button='left')
    pag.dragRel(size, 0, duration=duration, button='left')

    pag.moveRel(-size, size, duration=duration)
    pag.moveRel(size + seg, 0, duration=duration)