import time
import sys
import random

def loading():
    dots = [".", "..", "...", "....","....."]

    for _ in range(2):
        for d in dots:
            sys.stdout.write("\rLoading " + d + "   ")  
            sys.stdout.flush()
            time.sleep(0.15)

        sys.stdout.write("\r" + " " * 20 + "\r")
        sys.stdout.flush()

# loading()

def moving_dot():
    frames = ["●      ", " ○     ", "  ●    ", "   ○   ", "    ●  ", "     ○ "]
    for _ in range(2):
        for frame in frames:
            sys.stdout.write("\rLoading" + frame)
            sys.stdout.flush()
            time.sleep(0.15)
    sys.stdout.write("\r" + " " * 20 + "\r")
    sys.stdout.flush()

# moving_dot()


def wave():
    frames = ["~    ", " ~   ", "  ~  ", "   ~ ", "    ~", "   ~ ", "  ~  ", " ~   "]
    for f in frames:
        sys.stdout.write("\rLoading " + f)
        sys.stdout.flush()
        time.sleep(0.15)
    sys.stdout.write("\r" + " " * 20 + "\r")
    sys.stdout.flush()

# wave()


def pulse():
    frames = ["·    ", "••   ", "•••  ", " ••• ", "  •••", "   ••", "    ·", "     "]
    for _ in range(2):
        for f in frames:
            sys.stdout.write("\rLoading " + f)
            sys.stdout.flush()
            time.sleep(0.15)
    sys.stdout.write("\r" + " " * 20 + "\r")
    sys.stdout.flush()

# pulse()

