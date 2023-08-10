import tkinter as tk
from tkinter import ttk
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk
import customtkinter

class VistaPrincipal():
    def __init__(self, root, seleccionar_recital_callback=None, seleccionar_ubicacion_callback=None):
        self.root = root
        self.seleccionar_recital_callback = seleccionar_recital_callback
        self.seleccionar_ubicacion_callback = seleccionar_ubicacion_callback
        self.frame_mapa = tk.Frame(self.root, width=1000, height=1000,  bg="#45322e", borderwidth=10)
        self.frame_mapa.pack(side='right')

    
       
        customtkinter.set_appearance_mode("drack")
        self.frame_recitales = tk.Frame(self.root, width=900, height=600, bg="#45322e", borderwidth=10)
        
        self.frame_recitales.pack(side='left', fill='both', expand=True)

        # Placeholder para el mapa
        self.mapa = TkinterMapView(self.frame_mapa, width=600, height=600, corner_radius=0)
        self.mapa.set_position(-34.603312237051846, -58.378823684693614)
        self.mapa.set_zoom(16)
        self.mapa.pack(side='right')

        # Listbox para los locales
        self.lista_recitales = tk.Listbox(self.frame_recitales)
        self.lista_recitales.bind('<<ListboxSelect>>', seleccionar_recital_callback)
        self.lista_recitales.pack(fill='both', expand=True)

    def agregar_recital(self, Recital):
        nombre = Recital.nombre
        #artista =Recital.artista
        genero= Recital. genero
        fecha= Recital.fecha
        hora_inicio=Recital.hora_inicio
        hora_fin=Recital.hora_fin
        #descripcion=Recital.descripcion
        #imagen=Recital.imagen

        self.lista_recitales.insert(tk.END, nombre, genero, fecha, hora_inicio, hora_fin) #descripcion,#imagen)

    def agregar_marcador_mapa(self, latitud, longitud, texto, imagen=None):
        return self.mapa.set_marker(latitud, longitud, text=texto, image=imagen, command=self.seleccionar_ubicacion_callback)