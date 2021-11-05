# utils/display.py
import sys #import sys
import time #import time


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)
