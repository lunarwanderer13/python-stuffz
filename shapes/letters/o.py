import pyautogui as pag

# Setting up failsafe
pag.FAILSAFE = True

def o(size, duration):
    seg = size * (1 / 8)

    pag.moveRel(0, -seg, duration=duration)
    pag.dragRel(0, -seg * 6, duration=duration, button='left')
    pag.dragRel(seg, -seg, duration=duration, button='left')
    pag.dragRel(seg * 6, 0, duration=duration, button='left')
    pag.dragRel(seg, seg, duration=duration, button='left')
    pag.dragRel(0, seg * 6, duration=duration, button='left')
    pag.dragRel(-seg, seg, duration=duration, button='left')
    pag.dragRel(-seg * 6, 0, duration=duration, button='left')
    pag.dragRel(-seg, -seg, duration=duration, button='left')

    pag.moveRel(0, seg, duration=duration)
    pag.moveRel(size + seg, 0, duration=duration)