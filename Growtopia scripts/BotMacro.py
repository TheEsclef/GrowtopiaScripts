from pyautogui import *
import pyautogui
import time
import keyboard
import pyscreeze
import win32api, win32con
import win32gui

time.sleep(3)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#LGRID X:915 Y:1003
def start():
	click(915,1003)
	time.sleep(0.05)

def PlaceBlocks():
	click(1014,546)
	time.sleep(0.1)
	click(1083,550)
	time.sleep(0.05)

def BreakBlocks():
	keyboard.press("space")
	time.sleep(2.5)
	keyboard.release("space")
	time.sleep(0.05)

start()

while True:
    if keyboard.is_pressed("f7") != True:
        time.sleep(0.05)
        PlaceBlocks()
        time.sleep(0.4)
        BreakBlocks()
        time.sleep(0.1)
