from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con
import pyscreeze

#block no.1 left of player x= 920 y= 570
#block no.2 left of player x= 840 y= 570
#block no.1 right of player x = 1040 y= 570
#block no.2 right of player x = 1100 y= 570

PROGRAM = pyautogui.getWindowsWithTitle("Growtopia")[0]


# Q STARTS THE PROGRAM
# HOLDING O STOPS IT

time.sleep(5)

def breaksugar(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.8)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
PROGRAM.activate()

while 1:
    if keyboard.is_pressed("q"):
        while 1:
            if keyboard.is_pressed("o"):
                break
            else:
                breaksugar(960, 570)
                time.sleep(0.1)
                click(900, 1020)
                time.sleep(0.1)
                click(960, 570)
                time.sleep(0.1)
                click(810, 1020)
                time.sleep(0.1)
