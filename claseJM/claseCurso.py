#Victor Jose Peña Cordero


from claseAlumno import Alumno

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
                salida += f'{a.nom_alumno} = {a.notas_alumno}\n'
        else:
            salida = self.__alumnos
        return salida
    
    
    @property
    def listar_alumnos(self):
        salida = f'Alumnos del curso de {self.__nombre_curso}'
        if self.__alumnos:
            for alum in self.__alumnos:
                salida += '       ' + alum.nom_alumno +'\n'
        else:
            salida = f'El curso de {self.__nombre_curso} aun no tiene alumnos dados de alta'
        return salida


    @property
    def listar_alumnos_y_notas(self):
        '''lista los nombres de los alumnos del curso con sus notas parciales'''
        salida = f'Alumnos del curso de {self.__nombre_curso} con sus notas parciales'
        if self.__alumnos:
            for alum in self.__alumnos:
                n = self.__relleno(alum)
                salida += '       ' + alum.nom_alumno + n + ''.join(str(alum.notas_alumno))
        else:
            salida = f'El curso de {self.__nombre_curso} aun no tiene alumnos dados de alta'
        return salida



    def add_alumno(self, obj_alum):
        if type(obj_alum) is Alumno:
            self.__alumnos.append(obj_alum)




    @classmethod
    def desde_csv(cls, nom_curso, archivo):
        lista_de_obj_alumnos = []

        try:
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
        except:
                print('No se ha encontrado el archivo')
        else:
            return cls(nom_curso, lista_de_obj_alumnos)


    def __str__(self) -> str:
        salida = f'Curso de {self.__nombre_curso}/Alumnos y calificaciones: '
        for alum in self.__alumnos:
            salida +=alum.nom_alumno + '-'+ alum.calificacion + '\n'
        return salida


# ===============================================

curso = 'SSII'
archivo = '/home/victorjose/Github/Curso21-22/claseJM/archivo_alumnos.csv'


c = Curso(curso)
print(c.nombre_curso)
print(c.alumnos)

#clase2 = Curso('DAM')
#print(clase2.listar_alumnos)
clase = Curso.desde_csv(curso, archivo)
print(clase)
#alumno_nuevo = Alumno(['Juan María', 5, 6, 7, 8, 9, 10])
#clase.add_alumno(alumno_nuevo)
#print(clase)
#print(clase.alumnos_del_curso)
#print(clase.alumnos_y_notas)
