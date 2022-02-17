
ARCHIVO = '/home/victorjose/Github/Curso21-22/Victor/ejercicio_1/alumnos.csv'

class alumno():
    def __init__(self,) -> None:
        self.__nombre = ' ' 
        self.__notas = [ ]
        self.__calificacion = ' '

    def calificacion(self):
        nota = ''
        if self.__notas:
            notas_media = sum(self.__notas) / len(self.__notas) 
            if 0 < notas_media < 4:
                nota = 'Suspenso'
            elif 5 <= notas_media < 6:
                nota = 'Suficiente'
            elif 6 <= notas_media < 7:
                nota = 'Bien'
            elif 7 <= notas_media < 8:
                nota = 'Notable'
            elif 8 <= notas_media < 9:
                nota = 'Sobresaliente'
            elif 9 <= notas_media < 10:
                nota = 'Matricula Honor'
        else:
            nota = None
        return nota 


    @property
    def nombre_alumno(self):
        return self.__nombre

    @property
    def notas_alumno(self):
        return self.__notas

    @property
    def calificacion_alumno(self):
        return self.__calificacion


    @nombre_alumno.setter
    def nombre_alumno(self,nom_alumno):
        self.__nombre = nom_alumno

    @notas_alumno.setter
    def notas_alumno(self,not_alum):
        self.__notas = not_alum

    @calificacion_alumno.setter
    def calificacion_alumno(self,cali_alumn):
        self.__calificacion = cali_alumn
class Clase():
    def __init__(self,nombre) -> None:
        self.__nombre = nombre
        self.__alumnos = []


    def alumnos_lista(self):
        lista_de_alumnos = []
        with open(ARCHIVO, 'r') as leer:
            filas = leer.readlines()
            for alumno in filas:
                alumno = []
                lista_nombre_y_notas = alumno[0:-1].split(',')
                alumno.append(lista_nombre_y_notas[0])
                for nota in lista_nombre_y_notas[1:]:
                    alumno.append(float(nota))
                lista_de_alumnos.append(alumno)
        return lista_de_alumnos


c= Clase
print(c.alumnos_lista())