"""
MIT License

Copyright (c) 2024 Lunar Wanderer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

"""
Python program created by 月猫 / LunarWanderer月

Songs:
    - Bard's Adventure - Yu-Peng Chen
    - Tiny Light - Akari Kitō
    - Gravity Falls Theme - Brad Breeck
    - Gurenge - LiSa
    - Yoru Ni Kakeru - YAOSOBI (NOT FINISHED)

It works by pressing keys from Q to U, A to J and Z to M.
Then, a Genshin Lyre program(https://specy.github.io/genshinMusic) written by Specy(https://specy.github.io/) reads those keypresses and turns them to sounds, just like in the game.
There are many possibilities with it and people keep creating more and more songs - I've chosen some of them!
"""

try:
    # Libraries
    from colored import fg, attr # Colored text
    import time # Delays
    import random # Randomness
    from pynput import keyboard # Keyboard controller
    keyboard_controller = keyboard.Controller()
    import os # System


    # Songs
    from bardsAdventure import bardsAdventure
    from tinyLight import tinyLight
    from gravityFalls import gravityFalls
    from gurenge import gurenge
    from yoruNiKakeru import yoruNiKakeru
except ModuleNotFoundError as err:
    print(f'ModuleNotFoundError {err}')

def switchWindow():
    keyboard_controller.press(keyboard.Key.alt_l)
    keyboard_controller.press(keyboard.Key.tab)
    time.sleep(.125)
    keyboard_controller.release(keyboard.Key.alt_l)
    keyboard_controller.release(keyboard.Key.tab)

def main():
    while True:
        randomColors = []
        for i in range(10):
            randomColors.append(random.randint(1, 230))

        print(f'{fg(15)}0. {fg(randomColors[0])}R{fg(randomColors[1])}a{fg(randomColors[2])}n{fg(randomColors[3])}d{fg(randomColors[4])}o{fg(randomColors[5])}m {fg(randomColors[6])}S{fg(randomColors[7])}o{fg(randomColors[8])}n{fg(randomColors[9])}g{attr(0)}')
        print(f'{fg(15)}1. {fg(150)}Bard\'s Adventure{attr(0)}')
        print(f'{fg(15)}2. {fg(9)}Tiny Light{attr(0)}')
        print(f'{fg(15)}3. {fg(25)}Gravity Falls{attr(0)}')
        print(f'{fg(15)}4. {fg(53)}Gurenge(紅蓮華 / Red Lotus){attr(0)}') # \u7d05\u84ee\u83ef\u000d
        #print(f'{fg(15)}5. {fg(140)}Yoru Ni Kakeru(夜に駆ける / Racing Into The Night){attr(0)}') # \u591c\u306b\u99c6\u3051\u308b
        song = int(input(f'{fg(15)}Select which song to play: '))

        time.sleep(.5)

        switchWindow()

        time.sleep(.5)

        keyboard_controller.type('u')

        time.sleep(2.5)

        match song:
            case 0:
                song = random.randint(1, 4)
                match song:
                    case 1:
                        bardsAdventure()
                    case 2:
                        tinyLight()
                    case 3:
                        gravityFalls()
                    case 4:
                        gurenge()
                    #case 5:
                        #yoruNiKakeru()
                    case _:
                        raise ValueError(f'Incorrect input: {song}')
            case 1:
                bardsAdventure()
            case 2:
                tinyLight()
            case 3:
                gravityFalls()
            case 4:
                gurenge()
            #case 5:
                #yoruNiKakeru()
            case _:
                raise ValueError(f'Incorrect input: {song}')
        
        os.system('cls')

        time.sleep(.5)

        switchWindow()

        time.sleep(2.5)

if __name__ == '__main__':
    main()