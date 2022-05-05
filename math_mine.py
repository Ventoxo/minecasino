import os
import time
import pyautogui
import random

def follow(thefile):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


if __name__ == "__main__":
    while True:
        logfile = open("C:\\Users\\djako\\AppData\\Roaming\\.minecraft\\logs\\latest.log", "r")
        loglines = follow(logfile)
        for line in loglines:
            t = random.randint(2, 3)
            if "[CHAT] Сколько будет" in line:
                math_i = line[34::].split()
                i = 0
                sum_i = int(math_i[2]) + int(math_i[4][0:-1])
                time.sleep(t)
                pyautogui.press('t')
                pyautogui.write(str(sum_i), interval=0.25)
                pyautogui.press('enter')
                pyautogui.press('t')
                pyautogui.write("/pay Carrot1 100", interval=0.1)
                pyautogui.press('enter')

