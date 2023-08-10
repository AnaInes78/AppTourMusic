
import tkinter as tk

import customtkinter
import os
from PIL import Image

from vista_indice import Indice
from VentanaHistorial import VentanaHistorial
from buscador import Buscador
#from Busqueda import vista_principal



customtkinter.set_default_color_theme("blue") 

class App(customtkinter.CTk):
    
    width = 800
    height = 600
    #backgraund="#45322e"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("App Tour Musical")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        #self.configure(bg="#45322e")

        # cargar y crear la imagen de fondo
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(
            Image.open(current_path + "/recital.png"),
            size=(self.width, self.height),
        )
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)


         # crear el frame de login
        #self.backgraund= "#45322e"
        customtkinter.set_default_color_theme("blue") 
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=10, bg_color="#45322e")
        self.login_frame.grid(row=0, column=0, sticky="ns",)
        self.login_label = customtkinter.CTkLabel(
            self.login_frame, 
            text="Bienvenidos App Tour Musical \n Recitales Argentina",
            font=customtkinter.CTkFont("Roboto", size=20, weight="bold"),
        )
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.username_entry = customtkinter.CTkEntry(
            self.login_frame, width=200, placeholder_text="nombre de usuario"
        )
       
        
        self.login_button = customtkinter.CTkButton(
            self.login_frame, text="Indice de Recitales", command=self.login_event1, width=200
        )
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

        
        self.login_button2 = customtkinter.CTkButton(
            self.login_frame, text="Geolocalización de Recitales", command=self.login_event2, width=200
        )
        self.login_button2.grid(row=5, column=0, padx=30, pady=(15, 15))

        self.login_button3 = customtkinter.CTkButton(
            self.login_frame, text="Historial de Recitales", command=self.login_event, width=200
        )
        self.login_button3.grid(row=7, column=0, padx=30, pady=(15, 15))

        self.login_button4 = customtkinter.CTkButton(
            self.login_frame, text="Buscador de Recitales", command=self.login_event3, width=200
        )
        self.login_button4.grid(row=9, column=0, padx=30, pady=(15, 15))
        
        # crear el frame principal
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_label = customtkinter.CTkLabel(
            self.main_frame,
            text="Tour Musical\nPágina Principal",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.main_label.grid(row=8, column=0, padx=30, pady=(30, 15))
        self.back_button = customtkinter.CTkButton(
            self.main_frame, text="Volver", command=self.back_event, width=200
        )
        self.back_button.grid(row=10, column=0, padx=30, pady=(15, 15))



    def login_event1(self):
        vista_indice=Indice(self)
        vista_indice.mainloop()

    def login_event2(self): 
        Busqueda= vista_principal(self)
        #vista_principal.mainloop()

    def login_event(self):
        ventana_historial=VentanaHistorial(self)
        ventana_historial.mainloop()

    def login_event3(self):
        buscador=Buscador(self)
        buscador.mainloop()

    """self.login_frame.grid_forget()  # eliminar el frame de login
        self.login_frame.grid(
            row=8, column=0, sticky="nsew", padx=100
        )  # mostrar el frame principal"""

    def back_event(self):
        self.login_frame.grid_forget()  # eliminar el frame principal
        self.login_frame.grid(row=10, column=0, sticky="ns")  # mostrar el frame de login

if __name__ == "__main__":
    app = App()
    app.mainloop()

    