import PySimpleGUI as sg

def Main_Menu():
    sg.theme('LightGreen4')
    layout = [
        [sg.Button("Verify registered people", size=(20, 2), pad=(10, 5))],
        [sg.Button("Register a new person",size=(20, 2), pad=(10, 15))],
        [sg.Button("Exit", size=(10, 1), border_width=5)]
    ]
    return sg.Window("Main menu", layout=layout, finalize=True, size=(250, 200), element_justification='c')


window_open = Main_Menu()

while True:
    events, values = window_open.read()
    if events == sg.WINDOW_CLOSED:
        break
    if events == "Exit":
        sg.WINDOW_CLOSED
        break
