import pyautogui
from time import sleep


pyautogui.PAUSE = 2
pyautogui.press("win")
pyautogui.write("login.xlsx")
pyautogui.press("backspace")
pyautogui.press("enter")
sleep(3)
pyautogui.click(x=442, y=317, clicks=2, interval=0.2)
pyautogui.write("Lira")
pyautogui.click(x=418, y=365, clicks=2)
pyautogui.write("senha")
pyautogui.click(x=418, y=450, clicks=2)
