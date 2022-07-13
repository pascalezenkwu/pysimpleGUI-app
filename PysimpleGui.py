import PySimpleGUI as sg
import requests
from wikiAPI import *

layout = [
    [sg.Text("Search Keyword: "), sg.Input(key='INPUT')],
    [sg.Ok()],
    [sg.Text("", size=(0, 1), key='OUTPUT')]
]

window = sg.Window("Just a window", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Ok':
        name = values['INPUT']
        window['OUTPUT'].update(value=Search(name))

window.close()
