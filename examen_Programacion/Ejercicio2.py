#Victor José Peña Cordero
class Persona():

    __Nombre = None
    __Apellidos = None
    __Edad = None
    __DNI = None 
   
    def __init__(self,nombre,apellidos,edad,dni) -> None:
        self.Nombre = nombre
        self.Apellidos = apellidos
        self.Edad = edad
        self.DNI = dni

    def __str__(self) -> str:
        return (f'El nombre {self.Nombre} con apellido {self.Apellidos},Edad: {self.Edad},dni {self.DNI}')
  
    
pers = Persona('Victor José','Peña Cordero',21 ,'49034111-C')


print(pers)