#Victor Jose Peña Cordero

class Cancion():
    def __init__(self, nom_cancion) -> None:
        self.__nombre = nom_cancion
    
    @property
    def nombre_cancion(self):
        return self.__nombre

class CD():
    def __init__(self, lista=[]) -> None:
        self.canciones(lista)
        self.contador = len(self.canciones)


    @property
    def numeroCanciones(self):
        return self.contador

    @property
    def canciones(self, lista_canciones):
        return self._lis