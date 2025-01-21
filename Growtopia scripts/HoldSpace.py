from pyautogui import *
import pyautogui
import time
import keyboard
import pyscreeze
import win32api, win32con
import win32gui

time.sleep(3)

def BreakBlocks():
    keyboard.press("space")
    time.sleep(5)
    keyboard.release("space")
    time.sleep(0.1)

while True:
    BreakBlocks()
