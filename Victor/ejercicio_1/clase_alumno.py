#Victor Jose Peña Cordero
class Alumno():
    def __init__(self, alumno_lista=[]) -> None:
        if alumno_lista:
            self.__nombre = alumno_lista[0]
            if self.valida_notas(alumno_lista[1:]):
                self.__notas = alumno_lista[1:]
            
            self.__calificacion = self.calcula_calificacion()
        else:
            self.__nombre = ''
            self.__notas = []
            self.__calificacion = ''
            

    def __str__(self) -> str:
        return f'Alumno: {self.__nombre}, Calificaciones: {self.calificacion}'
        

    def calcula_calificacion(self):
        salida = ''
        if self.__notas:
            nota_media = sum(self.__notas) / len(self.__notas)
            if 0 < nota_media < 5:
                salida = 'SUSPENSO'
            elif 5 <= nota_media < 6:
                salida = 'SUFICIENTE'
            elif 6 <= nota_media < 7:
                salida = 'BIEN'
            elif 7 <= nota_media < 8:
                salida = 'NOTABLE'
            elif 8 <= nota_media < 9:
                salida = 'SOBRESALIENTE'
            else:
                salida = 'EXCELENTE'
        else:
            salida = None
        return salida

    def set_alumno(self, alumno):
        self.__nombre = alumno[0]
        for a in alumno[1:]:
            self.__notas.append(a)
        self.__calificacion = self.calcula_calificacion()
    
    @property
    def nomb_alumno(self):
        return self.__nombre
    @nomb_alumno.setter
    def nomb_alumno(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def notas_alumno(self):
        return self.__notas
    @notas_alumno.setter
    def notas_alumno(self, nuevas_notas_alum):
        if self.valida_notas(nuevas_notas_alum):
            self.__notas = nuevas_notas_alum
            self.__calificacion = self.calcula_calificacion()

    @property
    def calificacion(self):
        return self.__calificacion

    @staticmethod
    def valida_notas(lista_notas):
        valido = True
        if not lista_notas:
            valido = False
        else:
            for l in lista_notas:
                if not type(l) in (int,float) or not 0.0 <= l <= 10.0:
                    valido = False
        return valido


class Curso():
    def __init__(self, nom_curso, listado_alumnos=[]) -> None:
        self.__nombre_curso = nom_curso
        if listado_alumnos:
            self.__alumnos = listado_alumnos
        else:
            self.__alumnos = []


    @property
    def nombre_curso(self):
        return self.__nombre_curso

    @nombre_curso.setter
    def nombre_curso(self, nuevo_nombre):
        self.__nombre_curso = nuevo_nombre

    @property
    def alumnos(self):
        if self.__alumnos:
            salida = ''
            for a in self.__alumnos:
                salida += f'{a.nomb_alumno} = {a.notas_alumno}\n'
        else:
            salida = self.__alumnos
        return salida
    
    
    @property
    def listar_alumnos(self):
        salida = f' Alumnos del curso de {self.__nombre_curso}'
        if self.__alumnos:
            for alum in self.__alumnos:
                salida += '       ' + alum.nomb_alumno +'\n'
        else:
            salida = f'\n* * * El curso de {self.__nombre_curso} aun no tiene alumnos dados de alta * * *\n'
        return salida


    @property
    def listar_alumnos_y_notas(self):
        '''lista los nombres de los alumnos del curso con sus notas parciales'''
        salida = f'\n* * * Alumnos del curso de {self.__nombre_curso} con sus notas parciales * * *\n      -------\n'
        if self.__alumnos:
            for alum in self.__alumnos:
                n = self.__relleno(alum)
                salida += '       ' + alum.nom_alumno + n + ''.join(str(alum.notas_alumno)) + '\n'
        else:
            salida = f'\n* * * El curso de {self.__nombre_curso} aun no tiene alumnos dados de alta * * *\n'
        return salida



    def add_alumno(self, obj_alum):
            self.__alumnos.append(obj_alum)


    @classmethod
    def desde_csv(cls, nom_curso, archivo):
        lista_de_obj_alumnos = []

        with open(archivo, 'r') as manejador:
            filas = manejador.readlines()
            for fila_de_alumno in filas:
                alum = []
                lista_nombre_y_notas = fila_de_alumno[0:-1].split(',')
                alum.append(lista_nombre_y_notas[0])
                for nota in lista_nombre_y_notas[1:]:
                    if '.' in nota:
                        alum.append(float(nota))
                    else:
                        alum.append(int(nota))
                obj_alum = Alumno(alum) 
                lista_de_obj_alumnos.append(obj_alum)
    
        return cls(nom_curso, lista_de_obj_alumnos)


    def __max_long_nombres(self):
        max = 0
        for elem in self.__alumnos:
            longitud = len(elem.nom_alumno)
            if longitud > max:
                max = longitud
        return max + 2

    def __relleno(self, alumno):
        total = self.__max_long_nombres()
        salida = ' '
        for elem in range(total - len(alumno.nom_alumno)):
            salida += '-'
        salida += '> '
        return salida


    def __str__(self) -> str:
        salida = f'_______________________________________\nCurso de {self.__nombre_curso} - Alumnos y calificaciones:\n---------------------------------------\n'
        for alum in self.__alumnos:
            n = self.__relleno(alum)
            salida += '    '+ alum.nom_alumno + n + alum.calificacion + '\n'
        return salida


# ===============================================

curso = 'DAM'
archivo = 'C:/Users/avpen/Desktop/mi-git/Curso21-22/Victor/ejercicio_1/alumnos.csv'

a1 = Alumno(['Marcos', 5, 6, 7, 8, 9, 10])
a2 = Alumno(['Gabriel', 5, 6, 5, 6.5, 7, 6])
c = Curso(curso)
print(c.nombre_curso)
print(c.alumnos)

