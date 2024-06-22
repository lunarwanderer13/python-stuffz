import pyautogui as pag

# Setting up failsafe
pag.FAILSAFE = True

def a(size, duration):
    seg = size * (1 / 8)

    pag.dragRel(0, -seg * 7, duration=duration, button='left')
    pag.dragRel(seg, -seg, duration=duration, button="left")
    pag.dragRel(seg * 6, 0, duration=duration, button="left")
    pag.dragRel(seg, seg, duration=duration, button="left")
    pag.dragRel(0, seg * 7, duration=duration, button="left")
    pag.dragRel(0, -seg * 4, duration=duration, button="left")
    pag.dragRel(-seg * 7, 0, duration=duration, button="left")

    pag.moveRel(-seg, seg * 4)
    pag.moveRel(size + seg, 0, duration=duration)