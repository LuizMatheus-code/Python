from math import pi
import PySimpleGUI as sg

class PythonScreen:
    def __init__(self):
        layout = [
            [sg.Text('Pi = 3.14')],
            [sg.Text('Radius', size=(5, 0)), sg.Input(size=(22, 0), key=('Radius'))],
            [sg.Button('Result', key=('Result')), sg.Button('Cancel', key=('Cancel'))],
            [sg.Output()]
        ]
        self.window = sg.Window("Circle radius").layout(layout)
    def Start(self):
        while True:
            self.button, self.values = self.window.Read()
            if self.button == "Cancel":
                break
            radius = float(self.values['Radius'])
            area = pi * (radius**2)
            print('''Radius: {}\nArea: {:.2f}'''.format(radius, area))

open_screen = PythonScreen()
open_screen.Start()
