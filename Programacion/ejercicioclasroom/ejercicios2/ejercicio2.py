#Victor Jose Peña Cordero

class Coche():

    def __init__(self, marca='', modelo='', color='', num_puertas='', matricula='') -> None:
        self.__marca = marca
        self.__modelo = modelo  
        self.__color = color
        self.__num_puertas = num_puertas 
        self.__matricula = matricula    
    
    def __str__(self):
        return (f'La marca es: {self.__marca}, el modelo es: {self.__modelo}, el color es: {self.__color}, tiene {self.__num_puertas} puertas y la matrícula es:{self.__matricula}')
    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo
   
    @property
    def color(self):
        return self.__color

    @property
    def num_puertas(self):
        return self.__num_puertas

    @property
    def matricula(self):
        return self.__matricula
    @marca.setter
    def marca(self, marca):
        self.__marca = marca  

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @color.setter
    def color(self, color):
        self.__color = color   

    @num_puertas.setter
    def num_puertas(self, num_puertas):
        self.__num_puertas = num_puertas


    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
  



coche1 = Coche('Opel','Corsa','Blanco',5,'6560-JVP')
print(coche1)
coche2 = Coche()
coche2.marca = 'Opel'
coche2.modelo = 'Crossland'
coche2.color = 'Gris'
coche2.num_puertas = 5
coche2.matricula = '1440-JLN'
print(coche2)