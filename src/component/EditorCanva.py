import customtkinter as CTK
import src.core.app as app

class Instance:
    def __init__(self, master) -> None:
        self.frame = CTK.CTkFrame(master=master, fg_color="#808B96", bg_color="#808B96")
    def pack(self):
        self.frame.grid(row=0, column=1, sticky="nsew")