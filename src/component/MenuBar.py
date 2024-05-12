import tkinter as tk
import customtkinter as CTK
import src.core.app as app
import src.editor.data as data

bar = tk.Menu(app.root)
app.root.config(menu=bar)


file_menu = tk.Menu(bar, tearoff=0)

file_var = tk.IntVar()
file_menu.add_cascade(label="Nuevo")
file_menu.add_cascade(label="Abrir")
file_menu.add_cascade(label="Guardar", state="disabled")
file_menu.add_separator()
file_menu.add_cascade(label="Salir", state="disabled")

edit_menu = tk.Menu(bar, tearoff=0)
edit_menu.add_separator()

help_menu = tk.Menu(bar, tearoff=0)

help_menu.add_cascade(label="Acerca de...")

bar.add_cascade(label="Archivo", menu=file_menu)
bar.add_cascade(label="Editar", menu=edit_menu)
bar.add_cascade(label="Ayuda", menu=help_menu)