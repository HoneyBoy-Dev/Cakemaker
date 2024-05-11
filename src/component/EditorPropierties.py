import customtkinter as CTK
import src.core.app as app

class Instance:
    def __init__(self, master) -> None:
        self.frame = CTK.CTkFrame(master=master, fg_color="#2C3E50", bg_color="#2C3E50", width=200)
    def pack(self):
        self.frame.grid(row=0, column=0, rowspan=1, sticky="ns")