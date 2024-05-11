import customtkinter
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
