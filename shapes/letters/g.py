import pyautogui as pag

# Setting up failsafe
pag.FAILSAFE = True

def g(size, duration):
    seg = size * (1 / 8)

    pag.moveRel(seg * 4, -seg * 4, duration=duration)
    
    pag.dragRel(seg * 4, 0, duration=duration, button='left')
    pag.dragRel(0, seg * 3, duration=duration, button='left')
    pag.dragRel(-seg, seg, duration=duration, button='left')
    pag.dragRel(-seg * 6, 0, duration=duration, button='left')
    pag.dragRel(-seg, -seg, duration=duration, button='left')
    pag.dragRel(0, -seg * 6, duration=duration, button='left')
    pag.dragRel(seg, -seg, duration=duration, button='left')
    pag.dragRel(seg * 6, 0, duration=duration, button='left')
    pag.dragRel(seg, seg, duration=duration, button='left')

    pag.moveRel(-size, seg * 7, duration=duration)
    pag.moveRel(size + seg, 0, duration=duration)