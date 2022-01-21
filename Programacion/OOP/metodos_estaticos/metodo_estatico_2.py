class Estudiante():
    def __init__(self,nombre,apellidos) -> None:
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self) -> str:
        return f'Estudiante:{self.nombre} {self.apellidos}'

    @classmethod
    def estudiante_desde_json(cls,obj_json):
        estudiante = dict(obj_json)#{'nombre':'Paco','apellidos':'Lopez Garcia'}
        obj_estudiante = cls(estudiante['nombre'],estudiante['apellidos'])
        return obj_estudiante


    @classmethod
    def estudiante_desde_una_lista(cls,lista_estudiantes):
        lista_estudiantes = ['Paco','Lopez Garcia','Victor','Peña Cordero','Antonio','Perez Ruiz']
        obj_estudiante = cls(lista_estudiantes[0],lista_estudiantes[1])
        return obj_estudiante
    





x = Estudiante.estudiante_desde_json({'nombre':'Paco','apellidos':'Lopez Garcia'})
print(x)

y = Estudiante.estudiante_desde_una_lista(['Paco','Lopez Garcia'])
print(y)