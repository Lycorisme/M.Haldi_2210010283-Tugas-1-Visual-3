import PySimpleGUI as sg

sg.theme_background_color("#E2F1E7")
sg.theme_text_color("#243642")

layout = [
    [sg.Text("Selamat datang di kelas", background_color="#E2F1E7", text_color="#243642", justification="center", font=("Cambria", 25, "bold"))],
    [sg.Text("NPM     : 2210010283", background_color="#E2F1E7", text_color="#243642")],
    [sg.Text("Nama   : M.Haldi", background_color="#E2F1E7", text_color="#243642")],
    [sg.Text("Kelas    : 5E Regular Banjarmasin", background_color="#E2F1E7", text_color="#243642")],
    [sg.Text("Matkul : Pemrograman Visual 3", background_color="#E2F1E7", text_color="#243642")]
]

window = sg.Window(
    title="Profile",
    layout=layout,
    size=(430, 200),
    font=("Cambria", 16),
    finalize=True
)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
