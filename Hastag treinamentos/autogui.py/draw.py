import pyautogui

pyautogui.PAUSE = 1.5

pyautogui.alert("o programa vai iniciar")

pyautogui.press('win')

pyautogui.write('paint')

pyautogui.press('enter')

image_location = pyautogui.locateOnScreen('Hastag treinamentos\\autogui.py\circulo.png')

pyautogui.moveTo(image_location)

pyautogui.click(clicks=2)

pyautogui.move(0, 100)

pyautogui.drag(xOffset=400, yOffset=100, duration=3)
