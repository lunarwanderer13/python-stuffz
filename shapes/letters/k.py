import pyautogui as pag

# Setting up failsafe
pag.FAILSAFE = True

def k(size, duration):
    seg = size * (1 / 8)

    pag.dragRel(0, -size, duration=duration, button='left')
    pag.dragRel(0, seg * 4, duration=duration, button='left')
    pag.dragRel(size, -seg * 4, duration=duration, button='left')
    pag.dragRel(-size, seg * 4, duration=duration, button='left')
    pag.dragRel(size, seg * 4, duration=duration, button='left')

    pag.moveRel(seg, 0, duration=duration)