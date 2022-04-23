from turtle import back
import pyautogui 
import webbrowser as wb
import time
wb.open("web.whatsapp.com")
time.sleep(30)
for i in range(1000):
    pyautogui.press("i")
    pyautogui.press("space") 
    pyautogui.press("a")
    pyautogui.press("m")
    pyautogui.press("space")
    pyautogui.press("b")
    pyautogui.press("a")
    pyautogui.press("c")
    pyautogui.press("k")
    pyautogui.press("enter")
