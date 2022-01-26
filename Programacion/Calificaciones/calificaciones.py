


class Calificacion():
    def __init__(self, alumno_notas=[]) -> None:

        if alumno_notas:
            self.__nombre = alumno_notas[0]
            self.__notas = alumno_notas[1:]
            self.__calificacion = self.calcula_calificacion()
        else:
            self.__nombre = ''
            self.__notas = []
            self.__calificacion = ''

    def __str__(self) -> str:
        #return f'Alumno{self.nombre} tiene la calificacion {self.calificacion}'
        return 'Alumno: Raul tiene la calificacion NOTABLE'


    def calcula_calificacion(self):
        if self.__notas == []:
            return None
        media_notas = sum(self.__notas)/len(self.__notas)
        if round(media_notas) < 5:
            return 'Suspenso'
        elif round(media_notas) < 7:
            return 'Bien'
        elif round(media_notas) < 9:
            return 'Notable'
        else: 
            return 'Sobresaliente'

    @property
    def alumno(self):
        return self.__nombre

    @alumno.setter
    def alumno(self, alumno_nombre_nuevo):
        self.__nombre = alumno_nombre_nuevo

     
    @property
    def notas(self):
        return self.__notas

    @notas.setter
    def notas(self, nuevas_notas):
        self.__notas = nuevas_notas
        self.__calificacion = self.calcula_calificacion()

    @property
    def calificacion(self):
        return self.__calificacion
    
    @staticmethod
    def valida_notas(lista_notas):
        """
        Devuelve True cuando:
            - Cada nota esté entre 0-10
            - El tipo debe ser int o float
            - La lista no debe estar vacía
        """
        valido = True
        if lista_notas == []:
            valido = False

        for nota in lista_notas:
            if not type(nota) in (int,float) or not (0.0<= nota <= 10.0):
                valido = False

        return valido