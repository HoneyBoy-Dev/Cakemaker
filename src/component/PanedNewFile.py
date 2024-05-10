import customtkinter as CTK
import src.core.app as app
import src.editor.data as data

class Instance:
    def __init__(self) -> None:
        self.frame = CTK.CTkFrame(app.root, fg_color="#fff", width=200, height=200)
        self.title = CTK.CTkLabel(self.frame, text="Crea tu escena")

        self.container = CTK.CTkFrame(self.frame)
        self.title_name = CTK.CTkLabel(self.container, text="Nombra a tu escena")
        self.entry = CTK.CTkEntry(self.container)

        self.options = CTK.CTkFrame(self.frame, fg_color="transparent")
        self.option_cancel = CTK.CTkButton(self.options, text="Cancelar", width=50, command=self.destroy)
        self.option_apply = CTK.CTkButton(self.options, text="Aplicar", width=50, command=self.create_proyect)
    def pack(self):
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.title.pack(padx=130)
        self.container.pack(fill="x", expand=1, padx=5)
        self.title_name.pack()
        self.entry.pack(pady=15)
        self.options.pack(fill="x", expand=1)
        self.option_apply.pack(side="right", padx=5)
        self.option_cancel.pack(side="right", padx=5, pady=10)
    def create_proyect(self):
        self.content = self.entry.get()
        self.keys = [
            "/", "\\", "<", ">", '"', "'", ":", "|",
            "*", "#", "?", "~", "€", "$", "¬", "(",
            ")", "[", "]", "&"," "
        ]

        # no se usar el find o in.
        if self.content == "":
            self.title_name.configure(text="Los espacio en blanco no esta permitido", text_color="#FF0000")
        else:
            for i in range(len(self.keys)):
                for j in range(len(self.content)):
                    if self.content[j] == self.keys[i]:
                        self.title_name.configure(
                            text="caracter no permitido " + '" ' +self.keys[i] + ' "',
                            text_color="#FF0000"
                        )
                        break

    def destroy(self):
        self.frame.destroy()
        data.new_file = False
    