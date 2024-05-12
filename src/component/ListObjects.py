import customtkinter as CTK
import src.core.app as app
import src.editor.data as data

import src.component.ItemObject as ItemObject

class Instance:
    def __init__(self, master) -> None:
        self.frame = CTK.CTkFrame(
            master=master,
            fg_color="#2C3E50",
            bg_color="#2C3E50",
            width=200
        )

        self.list_container = CTK.CTkScrollableFrame(
            self.frame, 
            fg_color="#566573",
            scrollbar_button_color="#ABB2B9",
            scrollbar_button_hover_color="#808B96"
        )
        
        self.add_button = CTK.CTkButton(
            self.frame,
            text="Añadir",
            fg_color="#148F77",
            hover_color="#0E6251",
            command=self.command
        )
    def pack(self):
        self.frame.grid(row=0, column=2, sticky="ns")
        self.list_container.pack(fill="y", expand=1, padx=5, pady=5)
        self.add_button.pack(pady=5)
    
    def command(self):
        ItemObject.Instance(self.list_container).pack()