import PySimpleGUI as sg

sg.theme_background_color("#E2F1E7")
sg.theme_text_color("#243642")

susunan = [
    [sg.Push(), sg.Text("UNISKA MAAB", font=("Cambria", 24), background_color="#E2F1E7", text_color="#243642"), sg.Push()],
    [sg.Push(), sg.Text("BANJARMASIN", font=("Cambria", 18), background_color="#E2F1E7", text_color="#243642"), sg.Push()]
]

window = sg.Window(
    title="Elemen Text",
    layout=susunan,
    size=(430, 200),
    finalize=True
)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
