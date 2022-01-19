#Victor José Peña Cordero

class Rectangulo():

    def __init__(self, base=0, alto=0) -> None:
        self.__base = base
        self.__alto = alto 
     
    def __str__(self):
        return (f'La base del rectangulo es =  {self.__base} y el alto es = {self.__alto}')

    @property
    def base(self):
        return self.__base
    @property
    def alto(self):
        return self.__alto
    
    @base.setter
    def base(self, base):
        self.__base = base   

    
    @alto.setter
    def alto(self, alto):
        self.__alto = alto

    
    def area(self,base, alto):
        self.__base = base
        self.__alto = alto
        return self.__base * self.__alto

    @property
    def perimetro(self):
        return self.__base * 2 + self.__alto * 2

    

rec_1 = Rectangulo()
print(rec_1)

rec_2 = Rectangulo(2,3)
print(rec_2)

print(f'El area del rectángulo es: {rec_1.area}')
print(f'El perimetro del rectángulo es: {rec_1.perimetro}')