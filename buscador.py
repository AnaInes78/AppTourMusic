
import tkinter as tk
import json
from PIL import Image, ImageTk

class Buscador(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Buscador de Recitales")
        self.geometry("500x400")

        # Cargar los datos desde el archivo JSON y almacenarlos en self.recitales
        with open("recitales.json") as f:
            self.recitales = json.load(f)

        self.entry = tk.Entry(self)
        self.entry.pack(padx=10, pady=10)

        self.search_button = tk.Button(self, text="Buscar", command=self.realizar_busqueda)
        self.search_button.pack()

        # Crear un frame para el listado de resultados
        self.resultados_frame = tk.Frame(self)
        self.resultados_frame.pack(fill=tk.BOTH, expand=True)

    def realizar_busqueda(self):
        termino_busqueda = self.entry.get().lower()

        # Eliminar resultados anteriores
        for widget in self.resultados_frame.winfo_children():
            widget.destroy()

        for recital in self.recitales:
            if termino_busqueda in recital["artista"].lower():
                self.mostrar_resultado(recital)

    def mostrar_resultado(self, resultado):
        # Crear un enlace que muestre la ventana de detalles al hacer clic en el resultado
        def mostrar_ventana_detalles():
            ventana_resultado = tk.Toplevel(self)
            ventana_resultado.title(resultado["nombre"])

            # Código para mostrar los detalles del resultado
            label_nombre = tk.Label(ventana_resultado, text=f"Nombre: {resultado['nombre']}")
            label_nombre.pack()

            label_genero = tk.Label(ventana_resultado, text=f"Género: {resultado['genero']}")
            label_genero.pack()

            label_fecha = tk.Label(ventana_resultado, text=f"Fecha: {resultado['fecha']}")
            label_fecha.pack()

            label_hora_inicio = tk.Label(ventana_resultado, text=f"Hora de inicio: {resultado['hora_inicio']}")
            label_hora_inicio.pack()

            label_hora_fin = tk.Label(ventana_resultado, text=f"Hora de fin: {resultado['hora_fin']}")
            label_hora_fin.pack()

            label_descripcion = tk.Label(ventana_resultado, text=f"Descripción: {resultado['descripcion']}")
            label_descripcion.pack()

        # Crear un botón en el listado de resultados 
        boton_resultado = tk.Button(self.resultados_frame, text=resultado["nombre"], command=mostrar_ventana_detalles)
        boton_resultado.pack(fill=tk.X, padx=10, pady=5)

if __name__ == "__main__":
    app = Buscador(None)
    app.mainloop()