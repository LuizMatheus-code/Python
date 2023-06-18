import pyautogui
from time import sleep


pyautogui.PAUSE = 1

pyautogui.press('win')

pyautogui.write("notepad")

pyautogui.press("backspace")

pyautogui.press('enter')

pyautogui.click(x=586, y=350)

pyautogui.write("Login")

pyautogui.press("enter")

pyautogui.write("senha")
