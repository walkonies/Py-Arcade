import sys, os
import subprocess 
directory = os.getcwd()
def main():
    while True:
        game = input('$ ')
        if game == 'q':
            break

        cmd = f'python3 {directory}/{game}/driver.py'
        os.system(cmd)

if __name__ == '__main__':
    main()