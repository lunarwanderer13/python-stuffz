try:
    import pyautogui
    import time
    import lorem
except ModuleNotFoundError as err:
    print(f'ModuleNotFoundError {err}')

def main() -> None:
    x: int = int(input('How mad do you want your friend to be: '))

    time.sleep(5)

    for i in range(x):
        LoremText = lorem.paragraph()

        pyautogui.write(f'{i + 1}. {LoremText}')
        time.sleep(.1)

        pyautogui.press('enter')
        time.sleep(.1)

        time.sleep(.5)

if __name__ == '__main__':
    main()
