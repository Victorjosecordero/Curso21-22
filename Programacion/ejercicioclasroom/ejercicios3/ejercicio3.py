#Victor Jose Peña Cordero

class Tiempo():

    def __init__(self, horas=0, minutos=0, segundos=0) -> None:
        self.__horas = self.tiempo(horas)
        self.__minutos = self.tiempo(minutos)
        self.__segundos = self.tiempo(segundos)

    def __str__(self):
        return (f'Tiempo = {self.__horas}:{self.__minutos}:{self.__segundos}')

    
    @property
    def horas(self):
        return self.__horas
    @property
    def minutos(self):
        return self.__minutos
    @property
    def segundos(self):
        return self.__segundos

    @horas.setter
    def horas(self, horas):
        self.__horas = horas

    @minutos.setter
    def minutos(self, minutos):
        self.__minutos = minutos

    @segundos.setter
    def segundos(self, segundos):
        self.__segundos = segundos

    def tiempo(self, t):
        t_cad = int(t)
        
        return t_cad
    
      

t1=Tiempo(15,30,45)
print(t1)
    
