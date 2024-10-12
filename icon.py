import PySimpleGUI as sg

susunan = [
    [sg.Text("UNISKA MAAB", font=("Cambria", 24), text_color="#243642", background_color="#E2F1E7")],
    [sg.Text("BANJARMASIN", font=("Cambria", 18), text_color="#243642", background_color="#E2F1E7")]
]

window = sg.Window(
    title="New Icon", 
    layout=susunan, 
    element_justification="center", 
    icon="favicon.ico", 
    size=(430, 200), 
    background_color="#E2F1E7"
)

window.read()

window.close()
