#Victor José Peña Cordero
class Persona():
   
    def __init__(self,nombre,apellidos,edad,dni) -> None:
        self.Nombre = nombre
        self.Apellidos = apellidos
        self.Edad = edad
        self.DNI = dni

  
    
datos = Persona('victor','peña cordero',21 ,'49034111-C')
pers = (datos.Nombre, datos.Apellidos,datos.Edad ,datos.DNI) 

print(pers)