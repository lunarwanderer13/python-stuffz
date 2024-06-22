try:
    import keyboard
    import random
    import pyautogui as pag
except ModuleNotFoundError as err:
    print(f'ModuleNotFoundError {err}')

if __name__ == '__main__':
    while True:
        while keyboard.is_pressed('L'):
            interval: float = round(random.uniform(0.001, 0.075), 3)
            pag.click(interval=interval)
            print('L has been pressed. Clicking...')
