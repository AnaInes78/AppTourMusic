

import os
import tkinter as tk
from vista_principal import VistaPrincipal
from recital import Recital
from ubicacion import Ubicacion


from PIL import Image, ImageTk
import customtkinter


customtkinter.set_appearance_mode("dark")


class App(customtkinter.CTk):
    width = 900
    height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("App Tour Musical")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        # cargar y crear la imagen de fondo
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(
            Image.open(current_path + "/recital.png"),
            size=(self.width, self.height),
        )
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)



class ControladorPrincipal():
    def __init__(self, root):
        self.vista = VistaPrincipal(root, self.seleccionar_recital, seleccionar_ubicacion)
        self.recitales = Recital.cargar_recitales("recitales.json")
        self.ubicaciones = Ubicacion.cargar_ubicaciones("ubicaciones.json")
        self.marcadores = []
        self.imagenes = []

        self.cargar_recitales()
        self.cargar_imagenes()
        self.cargar_marcadores()
        
    def cargar_recitales(self):
        for recital in self.recitales:
            self.vista.agregar_recital(recital)
        
    def cargar_imagenes(self):
        for recital in self.recitales:
            imagen = ImageTk.PhotoImage(Image.open(f"views/{recital.imagen}").resize((200, 200)))
            self.imagenes.append(imagen)

    def cargar_marcadores(self):
        for ubicacion, recital in zip(self.ubicaciones, self.recitales):
            imagen = self.imagenes[ubicacion.id - 1]
            marcador = self.vista.agregar_marcador_mapa(ubicacion.latitud, ubicacion.longitud, recital.nombre, imagen)
            marcador.hide_image(True)
            self.marcadores.append(marcador)

    def seleccionar_recital(self, event):
        # Obtiene el índice del elemento seleccionado
        indice_seleccionado = self.vista.lista_recitales.curselection()
        # Obtiene el local seleccionado
        local_seleccionado = self.recitales[indice_seleccionado[0]]
        
        ubicacion_seleccionada = Ubicacion(0, 0, 0, "")
        
        # Busca la ubicación correspondiente al recital seleccionado
        for ubicacion in self.ubicaciones:
            if ubicacion.id == local_seleccionado.id_ubicacion:
                ubicacion_seleccionada = ubicacion
                break
        
        # Centra el mapa en la ubicación seleccionada
        self.vista.mapa.set_position(ubicacion_seleccionada.latitud, ubicacion_seleccionada.longitud)

        print(f"Latitud: {ubicacion_seleccionada.latitud}, Longitud: {ubicacion_seleccionada.longitud}")

def seleccionar_ubicacion(marcador):
    if marcador.image_hidden is True:
        marcador.hide_image(False)
    else:
        marcador.hide_image(True)
    print("Ubicación seleccionada: ", marcador.text)


class BuscadorFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.buscador = BuscadorFrame(self)
        self.buscador.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()