import PySimpleGUI as sg


def FolderExist(FolderName):
    try:
        verify = open(FolderName, 'rt')
        verify.close()
    except FileNotFoundError:
        return False
    else:
        return True


def CreateFolder(FolderName):
    try:
        opening = open(FolderName, 'wt+')
        opening.close()
    except:
        return False
    else:
        return True


def Main_Menu():
    sg.theme('LightGreen4')
    layout = [
        [sg.Button("Verify registered people", size=(20, 2), pad=(10, 5))],
        [sg.Button("Register a new person",size=(20, 2), pad=(10, 15))],
        [sg.Button("Exit", size=(10, 1), border_width=5)]
    ]
    return sg.Window("Main menu", layout=layout, finalize=True, size=(250, 200), element_justification='c')


def Verify_people():
    sg.theme('DarkGrey1')
    layout1 = [
        [sg.T("Name / Age")],
        [sg.Output(size=(40, 15), key="-OUTPUT-")],
        [sg.Button('Back', size=(10, 1), border_width=5,)]
    ]
    return sg.Window('People verificator', layout=layout1, finalize=True, size=(330, 330), element_justification="c")


def Register_new_person():
    sg.theme('LightBrown')
    layout2 = [
        [sg.Text('Name', size=(5,0)), sg.Input(size=(20, 0), key=('name value'))],
        [sg.Text('Age', size=(5,0)), sg.Input(size=(20, 0), key=('age value'))],
        [sg.Button("Save", size=(10, 1), border_width=3, pad=(10, 20)), sg.Button("Cancel", size=(10, 1), border_width=3, pad=(10, 20))]
    ]
    return sg.Window("People register", layout=layout2, finalize=True, size=(250, 130), element_justification="c")

window_open, verification_window, registering_window = Main_Menu(), None, None

while True:
    window, events, values = sg.read_all_windows()
    if window == window_open and events == sg.WINDOW_CLOSED:
        break
    if window == window_open and events == "Exit":
        sg.WINDOW_CLOSED
        break
    if window == window_open and events == "Verify registered people":
        existence = FolderExist('People registered.txt')
        if existence:
            window_open.hide()
            verification_window = Verify_people()
            verification_window['-OUTPUT-'].Update('')
            read_people = open('People registered.txt', 'rt')
            print(read_people.read())
        else:
            CreateFolder('People registered.txt')
            sg.popup("The file you're looking for doesn't exist. A new file was created right now. Try again.", title="Warning")
    if  window == verification_window and events == "Back":
        verification_window.hide()
        window_open.un_hide()
        verification_window = None
    if window == verification_window and events == sg.WINDOW_CLOSED:
        break
    if window == window_open and events == 'Register a new person':
        window_open.hide()
        registering_window = Register_new_person()
    if window == registering_window and events == sg.WINDOW_CLOSED:
        break
    if window == registering_window and events == "Cancel":
        window_open.un_hide()
        registering_window = None
    if window == registering_window and events == "Save":
        window_open.hide()
        existence = FolderExist('People registered.txt')
        if existence:
            writing = open('People registered.txt', 'at')
            writing.write(f'{values["name value"]} / {values["age value"]}\n')
            writing.close()
        else:
            CreateFolder('People registered.txt')
            sg.popup("The file you're using to save doesn't exist. A new file was created right now. Try again.", title="Error")
        registering_window.hide()
        window_open.un_hide()
        registering_window = None
sg.WINDOW_CLOSED
window.close()
