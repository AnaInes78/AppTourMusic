import json

class Recital:
    def __init__(self, nombre, artista, imagen, id_ubicacion, genero, fecha, hora_inicio,hora_fin,descripcion):
        self.nombre = nombre
        self.artista= artista
        self.imagen = imagen
        self.id_ubicacion = id_ubicacion
        self.genero= genero
        self.fecha= fecha
        self.hora_inicio= hora_inicio
        self.hora_fin= hora_fin
        self.descripcion= descripcion


    def a_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)

    @staticmethod
    def cargar_recitales(archivo_json):
        with open(archivo_json, "r") as archivo:
            datos = json.load(archivo)
        return [Recital.de_json(json.dumps(dato)) for dato in datos]