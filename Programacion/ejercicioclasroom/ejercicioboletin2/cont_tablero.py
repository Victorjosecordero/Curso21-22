
from random import randint

LIMITE_PUNTOS = 100
NUM_JUGADORES = 2
CARAS_DE_DADO = 6

class Jugador():
    
    def __init__(self) -> None:
        self.__puntos = 0
        self.__nombre = ''
    
    @property
    def puntos(self):
        return self.__puntos

    @puntos.setter
    def puntos(self,pts):
        self.__puntos += pts

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nomb):
        self.__nombre = nomb


class Partida():

    def __init__(self) -> None:
        self.__jugadores = []
        self.__lista_de__jugadores()

    def __lista_de__jugadores(self):
        for j in range(NUM_JUGADORES):
            jug = Jugador()
            jug.nombre = f'Jugador_{j}'
            self.__jugadores.append(jug)

    def jugar(self, fn_callback):
        seguir = True
        while seguir:
            for jugador in self.__jugadores:
                dado = randint(1,CARAS_DE_DADO)
                jugador.puntos = dado
                fn_callback(f'El jugador {jugador.nombre} lleva {jugador.puntos} puntos')
                if jugador.puntos >= LIMITE_PUNTOS:
                    fn_callback(f'Ganador: {jugador.nombre}')
                    seguir = False
                    break


def imprimir(cadena):
    print(cadena)

p = Partida()
p.jugar(imprimir)