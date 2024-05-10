import customtkinter as ctk
from src.core.app import *

""" Information """
import src.editor.data as data

""" COMPONENTS """
import src.component.MenuBar as MenuBar
import src.component.PanedNewFile as PanedNewFile



def open_window_new_file():
    if not data.new_file:
        paned = PanedNewFile.Instance()
        paned.pack()
        data.new_file = True
MenuBar.file_menu.entryconfig("Nuevo", command=open_window_new_file)