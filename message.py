import pyautogui
import time
import tkinter
time.sleep(4)
i = 0
while i <= 10:
    pyautogui.typewrite("Hii How are you")
    pyautogui.press("enter")
    i=i+1