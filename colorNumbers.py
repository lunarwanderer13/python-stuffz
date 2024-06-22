try:
    import time
    import random
    from colored import fg, attr
    import pyfiglet
    import keyboard
except ModuleNotFoundError as err:
    print(f'ModuleNotFoundError {err}')

num: int = 0
limit: int = 999999999

def main() -> None:
    for num in range(limit):
        num += 1
        col: int = random.randint(1,231)

        # Printing num's ascii
        ascii = pyfiglet.figlet_format(str(num))
        print(f'{fg(col)}{ascii}{attr(0)}')

        time.sleep(.5)

if __name__ == '__main__':
    main()
    # Ending the program
    print(f'{fg(1)}Reached the limit of {limit}{attr(0)}')
    keyboard.wait('shift + esc', suppress=True)
