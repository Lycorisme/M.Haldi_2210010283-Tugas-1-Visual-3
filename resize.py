import PySimpleGUI as sg

background_color = '#E2F1E7'
text_color = '#243642'

sg.theme_background_color(background_color)
sg.theme_text_color(text_color)

susunan = [
    [sg.Text("UNISKA MAAB", font=("Cambria", 24), justification='center', background_color=background_color)],
    [sg.Text("BANJARMASIN", font=("Cambria", 18), justification='center', background_color=background_color)]
]

window = sg.Window(
    title="New Icon", 
    layout=susunan, 
    element_justification="center",
    icon="favicon.ico", 
    resizable=True, 
    size=(430, 200),
    background_color=background_color 
)

window.read()
window.close()
