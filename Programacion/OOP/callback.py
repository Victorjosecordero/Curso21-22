import os

os.system('clear')

class Batidora():
    __motor = 0

    def enceder(self):
        self.__motor = 100
        print('Encendiendo')
    def apagar(self):
        self.__motor = 0
        print('Apagando')

    def acelerar(self,callback):
        self.__motor *= 2
        print('Acelerando')
        callback(self.__motor)
        


    def desacelerar(self,callback):
        self.__motor /= 2
        print('Desacelerando')
        callback(self.__motor)




######################################################3

def muestra_velocidad(velocidad):
    print(f'La velocidad de la batidora es {velocidad}')

def otra_funcion(velocidad):
    if velocidad > 400:
        print(f'Velocidad excesiva:{velocidad}')


b = Batidora()

b.enceder()
b.acelerar(muestra_velocidad)
b.acelerar(muestra_velocidad)
b.acelerar(muestra_velocidad)
b.acelerar(muestra_velocidad)
b.desacelerar(muestra_velocidad)
b.desacelerar(muestra_velocidad)
b.desacelerar(muestra_velocidad)
b.apagar()