#Victor Jose Peña Cordero

class Cancion():
    def __init__(self, nom_cancion) -> None:
        self.__nombre = nom_cancion
    
    @property
    def nombre_cancion(self):
        return self.__nombre

class CD():
    def __init__(self, lista=[]) -> None:
        self.canciones = lista
        self.contador = len(self.canciones)


    @property
    def numeroCanciones(self):
        return self.contador


    def nomb_cancion(self, pos):
        return self.canciones[pos-1]


    def graba_cancion(self, pos, cancion):
            self.canciones[pos-1] = cancion
        


    def añadir_cancion(self, cancion):
        self.canciones.append(cancion)
        self.contador += 1


    def __str__(self) -> str:
        salida = f'Hay {self.contador} Canciones. Las canciones son: '
        for i in range(1, self.contador+1):
            salida += f' {i}/{self.nomb_cancion(i).nombre_cancion}'
        return salida

c1 = Cancion('a')
c2 = Cancion('b')
c3 = Cancion('c')
d1 = CD([c1, c2, c3])
print(d1)
d1.añadir_cancion(Cancion('d'))
print(d1)
