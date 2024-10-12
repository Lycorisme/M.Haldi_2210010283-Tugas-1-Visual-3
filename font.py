import PySimpleGUI as sg

background_color = "#E2F1E7"
text_color = "#243642"

layout = [
    [sg.Column(
        [[sg.Text("FTI UNISKA", background_color=background_color, text_color=text_color, font=("Cambria", 24))],
         [sg.Text("FAKULTAS TEKNOLOGI INFORMASI", background_color=background_color, text_color=text_color)],
         [sg.Text("UNISKA MAB BANJARMASIN", background_color=background_color, text_color=text_color)]],
        background_color=background_color,
        element_justification='center',
        vertical_alignment='center',
        pad=(0, 0)
    )]
]

window = sg.Window(
    title="Font",
    layout=layout,
    background_color=background_color,
    size=(430, 200),
    font=("Cambria", 18),
    element_justification='center',
    finalize=True
)

window.read()

window.close()
