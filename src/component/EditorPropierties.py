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
            text="Nombre",
            text_color="#FFF"
        )

        self.name_object_entry = CTK.CTkEntry(
            self.container
        )

        self.propierties = CTK.CTkFrame(
            self.container,
            fg_color="#42566A"
        )

        self.x_label = CTK.CTkLabel(
            self.propierties,
            text="X",
            text_color="#FFF"
        )

        self.x_entry = CTK.CTkEntry(
            self.propierties,
            width=50
        )

        self.y_label = CTK.CTkLabel(
            self.propierties,
            text="Y",
            text_color="#FFF"
        )

        self.y_entry = CTK.CTkEntry(
            self.propierties,
            width=50
        )

        self.w_label = CTK.CTkLabel(
            self.propierties,
            text="width",
            text_color="#FFF"
        )

        self.w_entry = CTK.CTkEntry(
            self.propierties,
            width=50
        )

        self.h_label = CTK.CTkLabel(
            self.propierties,
            text="height",
            text_color="#FFF"
        )

        self.h_entry = CTK.CTkEntry(
            self.propierties,
            width=50
        )

        self.angle_label = CTK.CTkLabel(
            self.propierties,
            text="angle",
            text_color="#FFF"
        )

        self.angle_entry = CTK.CTkEntry(
            self.propierties,
            width=100
        )

        self.apply_button = CTK.CTkButton(
            self.container,
            text="Aplicar",
            fg_color="#148F77",
            hover_color="#0E6251"
        )

    def pack(self):
        self.frame.grid(row=0, column=0, rowspan=1, sticky="ns")
        self.container.pack(fill="y", expand=1, padx=5, pady=5)

        self.name_object_label.pack()
        self.name_object_entry.pack(padx=5)

        self.propierties.pack(expand=1, fill="both", padx=5, pady=5)
        self.propierties.columnconfigure(0, weight=1)
        self.propierties.columnconfigure(1, weight=1)

        self.x_label.grid(row=0, column=0)
        self.x_entry.grid(row=1, column=0, pady=5)

        self.y_label.grid(row=0, column=1)
        self.y_entry.grid(row=1, column=1, pady=5)

        self.w_label.grid(row=2, column=0)
        self.w_entry.grid(row=3, column=0, pady=5)

        self.h_label.grid(row=2, column=1)
        self.h_entry.grid(row=3, column=1, pady=5)

        self.angle_label.grid(row=4, column=0, columnspan=2)
        self.angle_entry.grid(row=5, column=0, columnspan=2, pady=5)

        self.apply_button.pack(pady=5)



