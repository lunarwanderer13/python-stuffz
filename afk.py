try:
    import pyautogui
    import random
    import time
    import keyboard
except ModuleNotFoundError as err:
    print(f'ModuleNotFoundError {err}')

pyautogui.FAILSAFE = True

def moveMouseAFK() -> None:
    while True:
        x = random.randint(300,700)
        y = random.randint(200,800)
        pyautogui.moveTo(x, y, duration=0.5)
        print(f'Moved mouse cursor to {x} - {y}')
        time.sleep(10)

if __name__ == '__main__':
    print('\nListetning for hotkeys...\n')
    keyboard.add_hotkey('alt + shift + L', moveMouseAFK, suppress=True)
    keyboard.wait('shift + esc')
