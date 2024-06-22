try:
    import random
    import keyboard
except ModuleNotFoundError as err:
    print(f'ModuleNotFoundError {err}')

def writeUwU() -> None:
    emojis: list[str] = ['UwU', 'U//w//U', 'U////U', 'OwO', 'O//w//O', 'O////O', '>w<', '>v<', '>_<', '>.<', '>-<', '>~<', '><', '>////<']
    text: str = random.choice(emojis)
    
    print(text)
    keyboard.write(text)

if __name__ == '__main__':
    print('\nListetning for hotkeys...\n')
    keyboard.add_hotkey('alt + shift + L', writeUwU, suppress=True)
    keyboard.wait('shift + esc')
