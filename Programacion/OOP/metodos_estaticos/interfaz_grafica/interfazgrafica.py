
from random import randint
from tkinter import Tk
from tkinter import ttk

raiz = Tk()

raiz.title('Juego de tablero')
raiz.geometry('400x300')
raiz.resizable(True,True)





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



button = ttk.Button(raiz, text="Pulsa para Jugar",
    command=lambda: tablero())
button.place(x=50, y=100)
#raiz.iconbitmap("/Programacion/OOP/metodos_estaticos/interfaz_grafica/750_logo_name.png")
raiz.mainloop() 