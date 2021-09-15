import PySimpleGUI as sg



class PythonScreen():
    def __init__(self):
        sg.change_look_and_feel('LightBlue2')
        layout = [
            [sg.Text('Name:', size=(5, 0)), sg.Input(size=(25, 0), key='Name')],
            [sg.Text('Age:', size=(5, 0)), sg.Input(size=(25, 0),key='Age')],
            [sg.Checkbox('Gmail',key='Gmail'), sg.Checkbox('Outlook',key='Outlook'), sg.Checkbox('Yahoo',key='Yahoo')],
            [sg.Text("Do you have a credit card?")],
            [sg.Radio('yes', "credit card", key="Yes"), sg.Radio('no', 'credit card', key='No')],
            [sg.Slider(range=(0, 255), default_value=0, orientation='h',size=(15, 20), key="sliderVelocity")],
            [sg.Button("Commit")],
            [sg.Output(size=(30, 9))]
        ]

        self.python_window = sg.Window('user data').layout(layout)

        

    def Start(self):
        while True:
            self.button, self.values = self.python_window.read()
            name = self.values['Name']
            age = self.values['Age']
            accept_gmail = self.values['Gmail']
            accept_outlook = self.values['Outlook']
            accpet_yahoo = self.values['Yahoo']
            yes_credit_card = self.values['Yes']
            no_credit_card = self.values['No']
            velocity = self.values['sliderVelocity']
            print(f'''name: {name}\nage: {age}\ngmail: {accept_gmail}\noutlook: {accept_outlook}\nyahoo: {accpet_yahoo}\nyes credit card: {yes_credit_card}\nno credit card: {no_credit_card}\nVelocity {velocity}''')


screen = PythonScreen()
screen.Start()
