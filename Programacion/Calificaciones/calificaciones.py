import re
from readline import parse_and_bind


class Calificacion():
    def __init__(self, alumno_notas=[]) -> None:

        self.calificacion = ''
        if alumno_notas:
            self.nombre = alumno_notas[0]
            self.notas = alumno_notas[1:]
            self.calificacion = self.calcula_calificacion()
        else:
            self.nombre = ''
            self.notas = []

    def __str__(self) -> str:
        #return f'Alumno{self.nombre} tiene la calificacion {self.calificacion}'
        return 'Alumno: Raul tiene la calificacion NOTABLE'


    def calcula_calificacion(self):
        if self.notas == []:
            return None
        media_notas = sum(self.notas)/len(self.notas)
        if round(media_notas) < 5:
            return 'Suspenso'
        elif round(media_notas) < 7:
            return 'Bien'
        elif round(media_notas) < 9:
            return 'Notable'
        else: 
            return 'Sobresaliente'
           
        
