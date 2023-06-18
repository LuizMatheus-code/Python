import pyautogui as p
from time import sleep

p.PAUSE = 0.5

p.alert("o código vai começar")

p.press("win")

p.write('chrome')

p.press("enter")

sleep(1.5)

p.write("https://drive.google.com/")

sleep(1)

p.press('enter')

sleep(3)

p.click(x=382, y=594, clicks=2, interval=0.5, button="left")

sleep(2)

p.hotkey("ctrl", "w")

p.alert("o código já finalizou")