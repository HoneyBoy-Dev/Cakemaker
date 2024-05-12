import customtkinter as CTK
import src.core.app as app

class Instance:
    def __init__(self, master) -> None:
        self.frame = CTK.CTkFrame(master=master, fg_color="#808B96", bg_color="#808B96")
        self.canvas = CTK.CTkCanvas(self.frame, bg="#797D7F")
    def pack(self):
        self.frame.grid(row=0, column=1, sticky="nsew")
        self.canvas.pack(fill="both", expand=1, padx=5, pady=5)