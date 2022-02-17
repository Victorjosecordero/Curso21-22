'''  Jose Manuel Perez Puig
Clase auxiliar que modela los datos de las canciones de un disco'''

class Cancion():
    def __init__(self, nom_cancion='') -> None:
        self.__nombre = nom_cancion
    
    @property
    def nombre_cancion(self):
        return self.__nombre

# =======================================