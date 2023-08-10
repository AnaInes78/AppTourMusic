import tkinter as tk
from VentanaHistorial import VentanaHistorial

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("App Tour Musical")
        # Crear botón Historial
        self.historial_button = tk.Button(self, text="Historial", command=self.abrir_historial)
        self.historial_button.pack()

    def abrir_historial(self):
        ventana_historial = VentanaHistorial(self)
        #ventana_historial.mainloop()

if __name__ == "__main__":
    app = App()
    app.mainloop()