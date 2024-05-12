import PIL.Image
import src.editor.data as data
import src.core.app as app
import customtkinter as CTK
import PIL

class Instance:
    def __init__(self, master) -> None:
        self.frame = CTK.CTkFrame(
            master=master,
            height=40,
            fg_color="transparent",
            bg_color="transparent"
        )

        self.button_object = CTK.CTkButton(
            self.frame,
            text="Object",
            fg_color="#148F77",
            hover_color="#0E6251"
        )

        self.icon = CTK.CTkImage(
            PIL.Image.open("res/icon/trash.png")
        )

        self.button_delete = CTK.CTkButton(
            self.frame,
            text="",image=self.icon,
            fg_color="#CB4335",
            hover_color="#78281F"
        )
        
    def pack(self):
        self.frame.pack()
        self.button_object.pack(side="left", padx=2, pady=2)
        self.button_delete.pack(side="right", padx=2)