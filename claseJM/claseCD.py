'''  Jose Manuel Perez Puig
clase que modela una lista de reproduccion'''

from claseCancion import Cancion
OVER = 'ERROR: En esa posición no hay ninguna canción. Número de canciones actual = '

class CD():
    def __init__(self, lista=[]) -> None:
        self.__canciones = lista
        self.__contador = len(self.__canciones)


    @property
    def numeroCanciones(self):
        '''metodo que devuelve el número de canciones, que corresponde al valor de la propiedad contador'''
        return self.__contador


    def dameCancion(self, pos):
        '''método que recibe un entero y devuelve la Canción almacenada en esa posición de la lista canciones'''
        if self.__valida_posicion(pos):
            return self.__canciones[pos-1]
        else:
            print(OVER + str(self.__contador))


    def grabaCancion(self, pos, obj_cancion):
        '''sustiruye la canción en la posición pasada, de la lista, por la canción pasada'''
        if self.__valida_posicion(pos):
            self.__canciones[pos-1] = obj_cancion
        else:
            print(OVER + str(self.__contador))


    def agregaCancion(self, obj_cancion):
        '''añade la canción pasada al final de la lista de canciones'''
        self.__canciones.append(obj_cancion)
        self.__contador += 1


    def elimina(self, pos):
        '''elimina de la lista de canciones la canción que haya en la posición pasada'''
        if self.__valida_posicion(pos):
            self.__canciones.pop(pos-1)
            self.__contador -= 1
        else:
            print(OVER + str(self.__contador))


    def __valida_posicion(self, pos):
        return pos <= self.__contador


    def __str__(self) -> str:
        salida = f'\n*** {self.__contador} Canciones actualmente en el Disco: \n    -----------------------------------\n'
        for i in range(1, self.__contador+1):
            salida += f'    n.{i} - {self.dameCancion(i).nombre_cancion}\n'
        return salida

# =======================================================
disco2 = CD()
print(disco2)
c1 = Cancion('Hoy no me puedo levantar')
c2 = Cancion('El pistolero ha llegado a la ciudad')
c3 = Cancion('We will rock you')
disco1 = CD([c1, c2, c3])
print(disco1.dameCancion(1).nombre_cancion +' , '+ disco1.dameCancion(2).nombre_cancion + ' , '+ disco1.dameCancion(3).nombre_cancion)
print(disco1)
disco1.elimina(3)
print(disco1)
disco1.agregaCancion(Cancion('Ojos Negros'))
print(disco1)
disco1.grabaCancion(1, Cancion('Sobreviviré'))
print(disco1)