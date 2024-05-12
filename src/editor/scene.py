import customtkinter as ctk
from src.core.app import *

""" Information """
import src.editor.data as data
import webbrowser

""" COMPONENTS """
import src.component.MenuBar as MenuBar
import src.component.PanedNewFile as PanedNewFile
import src.component.ListObjects as ListObjetcs


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
