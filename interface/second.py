import PySimpleGUI as sg

def login_window():
    sg.theme("DarkPurple5")
    layout = [
        [sg.Text('Name')],
        [sg.Input()],
        [sg.Button('Continue')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)


def ordering_window():
    sg.theme("DarkGreen4")
    layout = [
        [sg.Text('order')],
        [sg.Checkbox('Pizza', key='pizza chosen'), sg.Checkbox("Hamburguer", key='hamburguer chosen')],
        [sg.Button('Back'), sg.Button('Order now')]
    ]
    return sg.Window('Order now', layout=layout, finalize=True)

window1, window2 = login_window(), None

while True:
    window, event, values = sg.read_all_windows()
    if window == window1 and event == sg.WINDOW_CLOSED:
        break
    if window == window1 and event == "Continue":
        window2 = ordering_window()
        window1.hide()
    if window == window2 and event == "Back":
        window2.hide()
        window1.un_hide()
    if window == window2 and event == 'Order now':
        if values['pizza chosen'] == True and values['hamburguer chosen'] == True:
            sg.popup('a pizza and a hamburguer were ordered just now')
        elif values['pizza chosen']:
            sg.popup('a pizza was ordered just now')
        else:
            sg.popup('a hamburguer was ordered just now')
