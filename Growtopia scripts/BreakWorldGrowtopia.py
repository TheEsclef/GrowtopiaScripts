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


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def HoldSpace():
    pyautogui.keyDown("Space")
    time.sleep(1.8)
    pyautogui.keyUp("Space")

def BreakLeft():
    for i in range(50):
        time.sleep(0.1)
        pyautogui.keyDown("a")
        pyautogui.keyDown("Space")
        time.sleep(5)
        pyautogui.keyUp("Space")
        pyautogui.keyUp("a")
        if keyboard.is_pressed("o"):
            break

def BreakRight():
    for i in range(50):
        time.sleep(0.1)
        pyautogui.keyDown("d")
        pyautogui.keyDown("Space")
        time.sleep(5)
        pyautogui.keyUp("Space")
        pyautogui.keyUp("d")
        if keyboard.is_pressed("o"):
            break
        
def BreakDownL():
    #x20 y630  x20 y700
    for i in range(3):
        click(20, 630)

def BreakDownR():
    #x20 y630  x20 y700
    for i in range(3):
        click(1880, 630)

        
while 1:
    if keyboard.is_pressed("i"):
         BreakLeft()
    if keyboard.is_pressed("p"):
         BreakRight()
