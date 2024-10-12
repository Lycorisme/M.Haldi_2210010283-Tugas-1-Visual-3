import PySimpleGUI as sg

background_color = '#E2F1E7'
text_color = '#243642'

sg.theme_background_color(background_color)
sg.theme_text_color(text_color)

button_size = (15, 1)

layout = [
    [sg.Text("Contoh Button", font=("Cambria", 18), justification='center', background_color=background_color)],
    [sg.Button("Button Simpan", font=("Cambria", 18), size=button_size)],
    [sg.Button("Button Keluar", font=("Cambria", 18), size=button_size)]
]

window = sg.Window(
    title="Contoh Button", 
    layout=layout, 
    size=(430, 200),
    element_justification='center',
    resizable=True,
    background_color=background_color
)

kejadian, nilai = window.read()

print(kejadian, "=>", nilai)

window.close()
