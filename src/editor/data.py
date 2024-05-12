import customtkinter as CTK
import json

new_file = False
is_create_file = False

open_file = False

scene_name = ""
resource = {}


prefile = {
    "animations": {},
    "tiles": {},
    "objects": {}
}

def create(name):
    data_file = json.dumps(prefile)
    with open(name, 'w') as archivo:
        archivo.write(data_file)

def add_object():
    print("hello")

import src.component.MenuBar as MenuBar
def save_button_enable():
    MenuBar.file_menu.entryconfig("Guardar", state="active")
    MenuBar.file_menu.entryconfig("Salir", state="active")
