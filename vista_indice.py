

import tkinter as tk
import customtkinter
import json


class Indice(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Índice de Recitales")
        self.geometry("800x600")
        
        self.lista_recitales = tk.Listbox(self)
        self.lista_recitales.pack(fill='both', expand=True)

        # Cargar los datos desde el archivo JSON
        with open("recitales.json") as f:
            recitales = json.load(f)
        
        # Mostrar los nombres de los recitales en la lista
        for recital in recitales:
            self.lista_recitales.insert(tk.END, recital["nombre"])