import PySimpleGUI as sg

layout = [
    [sg.VPush()],
    [sg.Text("UNISKA MAAB", font=("Cambria", 24), text_color="#243642", background_color="#E2F1E7", justification='center')],
    [sg.Text("BANJARMASIN", font=("Cambria", 18), text_color="#243642", background_color="#E2F1E7", justification='center')],
    [sg.VPush()]
]

window = sg.Window(
    title="Elemen Text", 
    layout=layout, 
    size=(430, 200), 
    background_color="#E2F1E7",
    element_justification='center'
)

window.read()

window.close()
