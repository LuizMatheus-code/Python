import PySimpleGui as sg



layout = [
    [sg.Text("Consultar cotação da moeda")],
    [sg.InputText()],
    [sg.Button("Consultar"), sg.Button("Cancelar")],
    [sg.Text("A cotação")],
]

janela = sg.Window("Titulo", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED:
        break

janela.close()
