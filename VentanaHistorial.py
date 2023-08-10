
import tkinter as tk
import customtkinter
from PIL import Image
import os
import json
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")

class VentanaHistorial(tk.Toplevel):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Historial de Recitales")
        self.geometry("800x600")
        self.resizable(False,False)
        

        # Cargar los datos desde el archivo JSON
        with open("recitalesvistos.json") as f:
            self.recitales_data = json.load(f)

        # Cargar los comentarios y ánimos desde el diccionario (deberías cargarlos desde donde los almacenas)
        self.comentarios = {}  # Ejemplo: {"Recital 1": [("😃", "¡Excelente recital!"), ("😔", "No me gustó mucho...")]}
        
# cargar y crear la imagen de fondo
       # current_path = os.path.dirname(os.path.realpath(__file__))
        #self.bg_image = customtkinter.CTkImage(
        #    Image.open(current_path + "/recital.png"),
            #size=(800, 600),
        
        #self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        #self.bg_image_label.grid(row=0, column=0)

       
        # Crear un ListBox para mostrar los recitales
        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill=tk.BOTH, expand=True)
        for recital in self.recitales_data:
            self.listbox.insert(tk.END, recital["nombre"])

        # Crear un Entry para que el usuario ingrese comentarios
        self.comment_entry = tk.Entry(self)
        self.comment_entry.pack(fill=tk.X, )
        self.background="#A1A892"
        # Crear Radiobuttons para el señalador de ánimo
        self.bg="#E6D884"
        self.animo_var = tk.StringVar()
        self.animo_var.set("😃")  # Valor predeterminado
        self.animo_frame = tk.Frame(self)
        self.animo_frame.pack()
        tk.Radiobutton(self.animo_frame, text="😃", variable=self.animo_var, value="😃").pack(side=tk.LEFT)
        tk.Radiobutton(self.animo_frame, text="😔", variable=self.animo_var, value="😔").pack(side=tk.LEFT)

        # Crear un botón para agregar comentarios al recital seleccionado
        self.agregar_button = tk.Button(self, text="Agregar Comentario", command=self.agregar_comentario,  bg="#E6D884")
        self.agregar_button.pack()

        # Crear un Label para mostrar comentarios anteriores
       
        self.comentarios_label = tk.Label(self, text="Comentarios anteriores:")
        self.comentarios_label.pack()
        self.mostrar_comentarios()

    def agregar_comentario(self):
        seleccionado = self.listbox.curselection()
        if seleccionado:
            indice = seleccionado[0]
            recital = self.recitales_data[indice]["nombre"]
            comentario = self.comment_entry.get()
            animo = self.animo_var.get()
            if recital in self.comentarios:
                self.comentarios[recital].append((animo, comentario))
            else:
                self.comentarios[recital] = [(animo, comentario)]
            self.comment_entry.delete(0, tk.END)
            self.mostrar_comentarios()

    def mostrar_comentarios(self):
        comentarios_texto = "Comentarios anteriores:\n"
        for recital, comentarios in self.comentarios.items():
            for animo, comentario in comentarios:
                comentarios_texto += f"{recital} ({animo}): {comentario}\n"
        self.comentarios_label.config(text=comentarios_texto)

    # Crear un botón para abrir la ventana de reseña al seleccionar un recital
        self.ver_review_button = tk.Button(self, text="Ver Reseña", command=self.ver_review, width=20,  bg="#E6D884")
        self.ver_review_button.grid(row=3, column=1, padx=30, pady=(15, 0))

    def ver_review(self):
        seleccionado = self.listbox.curselection()
        if seleccionado:
            indice = seleccionado[0]
            recital = self.recitales_data[indice]["nombre"]

            # Intentar cargar la información de reseña desde el archivo Review.json
            try:
                with open("Review.json") as f:
                    review_data = json.load(f)
                if recital in review_data:
                    calificacion = review_data[recital]["Calificación"]
                    comentario = review_data[recital]["comentarios"]
                    messagebox.showinfo("Reseña", f"Reseña para '{recital}':\n\nCalificación: {calificacion}\nComentario: {comentario}")
                else:
                    messagebox.showinfo("Reseña", f"No se encontró reseña para '{recital}'.")
            except FileNotFoundError:
                messagebox.showinfo("Error", "No se encontró el archivo 'Review.json'.")


if __name__ == "__main__":
    app = VentanaHistorial(None)
    app.mainloop()

