from pygame import math


class Ejemplos():
    
    saludo = 'Hello'
    
    @classmethod
    def configurar(cls):
        return 'Metodo de clase',cls



    def suma(self,a,b):
        return a+b

e = Ejemplos()
print(e.suma(1,2))

print(Ejemplos.configurar())
