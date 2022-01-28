#Victor José Peña Cordero
from random import randint


class Tablero():
    
    def __init__(self) -> None:
        self.jugador1 = 0
        self.jugador2 = 0
        self.tirada_jugador1 = 0
        self.tirada_jugador2 = 0
        self.fin_partida = False
        self.dadojugador1 = randint(1,7)
        self.dadojugador2 = randint(1,7)

    
    def iniciar_partida(self):

        print('El juego empieza')
        while self.fin_partida is False:


            print(f'Jugador 1 tira un dado y sale el numero: {self.dadojugador1}' )

            self.jugador1 += self.dadojugador1
            self.tirada_jugador1 += 1
            print(f'Jugador: 1 Tirada: {self.tirada_jugador1} Puntuacion: {self.jugador1}')

            print(f'Jugador 2 tira un dado y sale el numero: {self.dadojugador2}')

            self.jugador2 += self.dadojugador2
            self.tirada_jugador2 += 1
            print(f'Jugador: 2 Tirada: {self.tirada_jugador2} Puntuacion: {self.jugador2}')

            if  self.jugador1 >= 100:
                self.fin_partida = True
                print('¡¡El jugador 1 HA GANADO!!')
                print(f'Puntuacion final: \n Jugador 1: {self.jugador1} \n Jugador 2: {self.jugador2} ')
            elif self.jugador2 >= 100:
                self.fin_partida = True
                print('¡¡El jugador 2 HA GANADO!!')
                print(f'Puntuacion final: \nJugador 1:{self.jugador1} \nJugador 2: {self.jugador2} ')
            else:
                pass

t=Tablero()
t.iniciar_partida()