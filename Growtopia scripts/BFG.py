from pyautogui import *
import pyautogui
import time
import keyboard
import pyscreeze
import win32api, win32con
import win32gui

time.sleep(2)
start = 0

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def holdclick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(1.4)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def CheckEnd():
    if keyboard.is_pressed("F7"):
        if start == 0:
            start = 1
        elif start == 1:
            start = 0

def PlaceBlocks():
    click(915,1003)
    CheckEnd()
    time.sleep(0.1)
    CheckEnd()
    click(900,367)
    CheckEnd()
    time.sleep(0.1)
    CheckEnd()
    click(879,716)
    CheckEnd()
    time.sleep(0.1)
    click(800,718)
    CheckEnd()
    time.sleep(0.1)
    click(800,643)
    CheckEnd()
    time.sleep(0.1)
    click(870,643)
    CheckEnd()
    time.sleep(0.1)
    click(880,550)
    CheckEnd()
    time.sleep(0.1)
    click(800,530)
    CheckEnd()
    time.sleep(0.1)
    click(800,450)
    CheckEnd()
    time.sleep(0.1)
    click(900,450)
    CheckEnd()
    time.sleep(0.1)
    click(808,380)
    CheckEnd()
    time.sleep(0.1)

def BreakBlocks():
    click(816,1003)
    CheckEnd()
    time.sleep(0.1)
    holdclick(900,367)
    CheckEnd()
    time.sleep(0.05)
    holdclick(879,716)
    CheckEnd()
    time.sleep(0.05)
    holdclick(800,718)
    CheckEnd()
    time.sleep(0.05)
    holdclick(800,643)
    CheckEnd()
    time.sleep(0.05)
    holdclick(870,643)
    CheckEnd()
    time.sleep(0.05)
    holdclick(880,550)
    CheckEnd()
    time.sleep(0.05)
    holdclick(800,530)
    CheckEnd()
    time.sleep(0.05)
    holdclick(800,450)
    CheckEnd()
    time.sleep(0.05)
    holdclick(900,450)
    CheckEnd()
    time.sleep(0.05)
    holdclick(808,380)
    CheckEnd()
    time.sleep(0.05)


while True:
    if keyboard.is_pressed("F7"):
        if start == 0:
            start = 1
            time.sleep(0.2)
        elif start == 1:
            start = 0
            time.sleep(0.2)
    if start == 1:
        PlaceBlocks()
        time.sleep(0.1)
        BreakBlocks()
        time.sleep(0.1)

#LGRID X:915 Y:1003
#FIST  X:816 Y:1003

#block1      900,367
#block2      879,716
#block3      800,718
#block4      800,643
#block5      870,643
#block6      880,550
#block7      800,530
#block8      800,450
#block9      900,450
#block10     808,380
