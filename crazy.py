try:
    from colored import fg
    import time
except ModuleNotFoundError as err:
    print(f'ModuleNotFoundError {err}')

def main() -> None:
    while True:
        print(f'{fg(1)}Crazy?')
        time.sleep(1.25)
        print(f'{fg(2)}I was crazy once.')
        time.sleep(1.25)
        print(f'{fg(3)}They locked me in a room.')
        time.sleep(1.25)
        print(f'{fg(4)}A rubber room.')
        time.sleep(1.25)
        print(f'{fg(5)}A rubber room with rats.')
        time.sleep(1.25)
        print(f'{fg(6)}The rats made me crazy.')
        time.sleep(1.25)

if __name__ == '__main__':
    main()
