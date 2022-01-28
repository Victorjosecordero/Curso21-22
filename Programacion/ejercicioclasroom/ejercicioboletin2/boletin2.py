"""
Hacer un programa para simular un juego de tablero sencillo:
        - Habrá dos jugadores.
        - Por turnos, cada uno tira un dado y se van sumando sus puntuaciones.
        - El primero que llegue a 100 puntos gana.
       
El programa debe simular las tiradas de los dados e imprimir el resultado de cada tirada.
Ejemplo: Jugador: 1 Tirada: 17 Puntos: 45
Cuando gane uno de los jugadores debe imprimir: ¡¡El jugador X HA GANADO!!
Se debe entregar:
        - Programa en versión funcional (sin clases)
        - Programa en versión orientada a objetos (usando clases)
NOTA: ES necesario demostrar que el programa funciona, con pruebas unitarias (recomendado) o de alguna otra forma.
"""
#Victor José Peña Cordero
from random import randint


def tablero():

    jugador1 = 0
    jugador2 = 0
    tirada_jugador1 = 0
    tirada_jugador2 = 0
    fin_partida = False
    dadojugador1 = randint(1,6)
    dadojugador2 = randint(1,6)

    print('El juego empieza')
    while fin_partida is False:


        print(f'Jugador 1 tira un dado y sale el numero: {dadojugador1}' )

        jugador1 += dadojugador1
        tirada_jugador1 += 1
        print(f'Jugador: 1 Tirada: {tirada_jugador1} Puntuacion: {jugador1}')

        print(f'Jugador 2 tira un dado y sale el numero: {dadojugador2}')

        jugador2 += dadojugador2
        tirada_jugador2 += 1
        print(f'Jugador: 2 Tirada: {tirada_jugador2} Puntuacion: {jugador2}')

        if jugador1 >= 100:
            fin_partida = True
            print('¡¡El jugador 1 HA GANADO!!')
            print(f'Puntuacion final: \n Jugador 1: {jugador1} \n Jugador 2: {jugador2} ')
        elif jugador2 >= 100:
            fin_partida = True
            print('¡¡El jugador 2 HA GANADO!!')
            print(f'Puntuacion final: \nJugador 1:{jugador1} \nJugador 2: {jugador2} ')
        else:
            pass


tablero()