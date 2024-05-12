import customtkinter as CTK
import src.core.app as app

class Instance:
    def __init__(self, master) -> None:
        self.frame = CTK.CTkFrame(
            master=master,
            fg_color="#2C3E50",
            bg_color="#2C3E50",
            width=200
        )

        self.container = CTK.CTkFrame(
            master=self.frame,
            fg_color="#566573",
            bg_color="transparent"
        )

        self.name_object_label = CTK.CTkLabel(
            self.container,
            text="Nombre"
        )

    def pack(self):
        self.frame.grid(row=0, column=0, rowspan=1, sticky="ns")
        self.container.pack()

        self.name_object_label.grid(row=0, column=0)