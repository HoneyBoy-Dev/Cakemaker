import customtkinter as ctk
from src.core.app import *

""" Information """
import src.editor.data as data
import webbrowser

""" COMPONENTS """
import src.component.MenuBar as MenuBar
import src.component.PanedNewFile as PanedNewFile
import src.component.EditorPropierties as EditorPropierties
import src.component.EditorCanva as EditorCanva
import src.component.ListObjects as ListObjects


def open_window_new_file():
    if not data.new_file:
        paned = PanedNewFile.Instance()
        paned.pack()
        data.new_file = True
MenuBar.file_menu.entryconfig("Nuevo", command=open_window_new_file)

# Documentation
def open_tab_browser():
    webbrowser.open("https://github.com/HoneyBoy-Dev/cakemaker")
MenuBar.help_menu.entryconfig("Acerca de...", command=open_tab_browser)

frame = ctk.CTkFrame(root)
frame.pack(expand=1, fill="both")

frame.rowconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

editor_propierties_bar = EditorPropierties.Instance(frame)
editor_propierties_bar.pack()

editor_canvas_bar = EditorCanva.Instance(frame)
editor_canvas_bar.pack()

list_objects_bar = ListObjects.Instance(frame)
list_objects_bar.pack()