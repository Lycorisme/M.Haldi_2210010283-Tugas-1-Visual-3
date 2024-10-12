import PySimpleGUI as sg

sg.theme_background_color("#E2F1E7")
sg.theme_text_color("#243642")

layout = [
    [sg.Text("TEKNOLOGI INFORMASI", size=(25, 1), justification="center", background_color="#E2F1E7", text_color="#243642")],
    [sg.Text("TEKNOLOGI INFORMASI", size=(25, 1), justification="left", background_color="#E2F1E7", text_color="#243642")],
    [sg.Text("TEKNOLOGI INFORMASI", size=(25, 1), justification="right", background_color="#E2F1E7", text_color="#243642")],
    [sg.Text("TEKNOLOGI INFORMASI " * 2, size=(25, 2), justification="center", background_color="#E2F1E7", text_color="#243642")],
    [sg.Text("UNISKA MAB BANJARMASIN", text_color="#FFCC00", background_color="#E2F1E7")]
]

window = sg.Window(
    title="Profile",
    layout=layout,
    size=(430, 200),
    font=("Cambria", 18),
    finalize=True
)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
