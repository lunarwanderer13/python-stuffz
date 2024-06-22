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
Shape Drawer made by 月猫
using pyautogui to drag the cursor
i recommend using MS Paint for testing
"""

try:
    # Libraries
    from colored import fg, attr
    import pyautogui as pag
    import time
    import math

    # Importing shapes
    from shapes.square import square
    from shapes.spiral import spiral
    from shapes.triangle import triangle
    from shapes.heart import heart
    from shapes.heartbeat import heartbeat
    from shapes.star import star

    # Importing lines
    from lines.solid import solid
    from lines.dashed import dashed

    # Importing letters
    from letters.a import a
    from letters.b import b
    from letters.c import c
    from letters.d import d
    from letters.e import e
    from letters.f import f
    from letters.g import g
    from letters.h import h
    from letters.i import i
    from letters.j import j
    from letters.k import k
    from letters.l import l
    from letters.m import m
    from letters.n import n
    from letters.o import o
    from letters.p import p
except ModuleNotFoundError as err:
    print(f'ModuleNotFoundError {err}')

# Setting up failsafe
pag.FAILSAFE = True

# Main function
def main():
    # Looping the program
    while True:
        # Printing the list of available shapes
        print('possible shapes: square | spiral | triangle | heart | heartbeat | star | line | letter')

        shape:str = input(f'{fg(225)}Which shape would you like to draw: {attr(0)}')

        # The lenght of one cursor movement
        duration:float = .25

        # Drawing the shapes
        match shape:
            case "square":
                size:int = int(input('How big should it be: '))
                square(size, duration)
            case "spiral":
                spiral(duration)
            case "triangle":
                size:int = int(input('How big should it be: '))
                triangle(size, duration)
            case "heart":
                size:int = int(input('How big should it be: '))
                heart(size, duration)
            case "heartbeat":
                heartbeat(duration)
            case "star":
                size:int = int(input('How big should it be: '))
                star(size, duration)
            case "line":

                print('possible lines: solid | dashed')

                line:str = input(f'{fg(225)}Which line would you like to draw: {attr(0)}')
                lenght:int = int(input('How long should the line be: '))

                match line:
                    case "solid":
                        solid(lenght, duration)
                    case "dashed":
                        dashed(lenght, duration)
                    case _:
                        raise ValueError(f'{fg(1)}Incorrect input: {line}{attr(0)}')
            case "letter":

                print('possible letters: alphabet | a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p')

                letter:str = input(f'{fg(225)}Which letter would you like to draw: {attr(0)}')
                size:int = int(input('How big should a letter be: '))

                # Rounding the size down so it's always divisible by 8, because there are 8 segments
                size:int = math.floor(size / 8) * 8

                # Cooldown before the start of drawing
                time.sleep(5)

                match letter:
                    case "alphabet":
                        a(size, duration)
                        b(size, duration)
                        c(size, duration)
                        d(size, duration)
                        e(size, duration)
                        f(size, duration)
                        g(size, duration)
                        h(size, duration)
                        i(size, duration)
                        j(size, duration)
                        k(size, duration)
                        l(size, duration)
                        m(size, duration)
                        n(size, duration)
                        o(size, duration)
                        p(size, duration)
                    case "a":
                        a(size, duration)
                    case "b":
                        b(size, duration)
                    case "c":
                        c(size, duration)
                    case "d":
                        d(size, duration)
                    case "e":
                        e(size, duration)
                    case "f":
                        f(size, duration)
                    case "g":
                        g(size, duration)
                    case "h":
                        h(size, duration)
                    case "i":
                        i(size, duration)
                    case "j":
                        j(size, duration)
                    case "k":
                        k(size, duration)
                    case "l":
                        l(size, duration)
                    case "m":
                        m(size, duration)
                    case "n":
                        n(size, duration)
                    case "o":
                        o(size, duration)
                    case "p":
                        p(size, duration)
                    case _:
                        raise ValueError(f'{fg(1)}Incorrect input: {letter}{attr(0)}')
            case _:
                raise ValueError(f'{fg(1)}Incorrect input: {shape}{attr(0)}')

if __name__ == '__main__':
    main()