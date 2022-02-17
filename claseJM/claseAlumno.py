'''  Jose Manuel Perez Puig
Clase para modelar una lista de libros con funcionalidades típicas'''

class Alumno():
    def __init__(self, alumno_lista=[]) -> None:
        if alumno_lista:
            self.__nombre = alumno_lista[0]
            if self.valida_notas(alumno_lista[1:]):
                self.__notas = alumno_lista[1:]
            else:
                raise Exception('Notas no válidas')
            self.__calificacion = self.calcula_calificacion()
        else:
            self.__nombre = ''
            self.__notas = []
            self.__calificacion = ''
            

    def __str__(self) -> str:
        return f'El Alumno: {self.__nombre} tiene la calificación: {self.calificacion}'
        

    def calcula_calificacion(self):
        salida = ''
        if self.__notas:
            nota_media = sum(self.__notas) / len(self.__notas)
            if 0 < nota_media < 4.9:
                salida = 'SUSPENSO'
            elif 5 <= nota_media < 5.5:
                salida = 'SUFICIENTE'
            elif 5.5 <= nota_media < 6.5:
                salida = 'BIEN'
            elif 6.5 <= nota_media < 8.5:
                salida = 'NOTABLE'
            elif 8.5 <= nota_media < 9.5:
                salida = 'SOBRESALIENTE'
            else:
                salida = 'EXCELENTE'
        else:
            salida = None
        return salida

    def set_alumno(self, alum):
        self.__nombre = alum[0]
        for elem in alum[1:]:
            self.__notas.append(elem)
        self.__calificacion = self.calcula_calificacion()
    
    @property
    def nom_alumno(self):
        return self.__nombre
    @nom_alumno.setter
    def nom_alumno(self, nuevo_nom_alum):
        self.__nombre = nuevo_nom_alum

    @property
    def notas_alumno(self):
        return self.__notas
    @notas_alumno.setter
    def notas_alumno(self, nuevas_notas_alum):
        if self.valida_notas(nuevas_notas_alum):
            self.__notas = nuevas_notas_alum
            self.__calificacion = self.calcula_calificacion()
        else:
            raise Exception('Notas no válidas')

    @property
    def calificacion(self):
        return self.__calificacion

    @staticmethod
    def valida_notas(lista_notas):
        # verdadero si son validas (float entre 0 y 10) y false si no lo son
        # Falso para tipo distinto a int o float o lista vacia
        valido = True
        if not lista_notas:
            valido = False
        else:
            for elem in lista_notas:
                if not type(elem) in (int,float) or not 0.0 <= elem <= 10.0:
                    valido = False
        return valido
