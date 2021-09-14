import PySimpleGUI as sg
from random import randint
import back

sg.theme('SystemDefault')


def front():
    flayout = [
        [sg.Text('Bem vindo')], #row 1
        [sg.Button('Entrar'), sg.Button('Sair')] #row2
    ]

    window = sg.Window("title", flayout, size=(500, 100), element_justification='center')
    button, values = window.read()

    if button == "Entrar":
        window.close()
    
    if button == "Sair":
        sg.WIN_CLOSED


layout = [
    [sg.Text('Name:'), sg.InputText('', key='-NAME-')],
    [sg.Button('Add')],
    [sg.Text('')],
    [sg.Text('Registered staff')],
    [sg.Listbox("NAME", size=(50, 10), key='-BOX-')],
    [sg.Button('Delete'), sg.Button('Exit')]
]

front()

window = sg.Window('main page', layout)

while True:
    button, values = window.read()

    if button == "Add":
        ID = randint(1, 999)
        NAME = values['-NAME-'].capitalize()

        if NAME != '':
            back.write(ID, NAME)
        
        window.find_element('-NAME-').Update('')
