class Racional():
    numerador1 = None
    numerador2 = None
    denominador1 = None
    denominador2 = None
    numerador_resultado = None
    mcm = None
    #contructor que admita numerador y denominador
    #contructor sin parametros
    #metodos Getters y setters
    #Suma,resta,Multiplicacion y division
    def __init__(self, num1, den1, num2, den2) -> None:
            self.numerador1 = int(num1)
            self.denominador1 = int(den1)
            self.numerador2 = int(num2)
            self.denominador2 = int(den2)

    def __str__(self):
        return str(self.numerador1) + "/" + str(self.denominador1)

    def equivalente(self) -> bool:
        return self.denominador1 == self.denominador2 and self.numerador1 == self.numerador2
    
    def maximo_comun_divisor(self, a, b):
        temporal = 0
        while b != 0:
            temporal = b
            b = a % b
            a = temporal
        return a

    def minimo_comun_multiplo(self, a, b):
        return (a * b) / self.maximo_comun_divisor(a, b)

    def suma(self) -> 'Fraccion':
        mcm = self.minimo_comun_multiplo(self.denominador1, self.denominador2)
        diferencia_self = mcm/self.denominador1
        diferencia_otra = mcm/self.denominador2
        numerador_resultado = (diferencia_self*self.numerador1) + \
        (diferencia_otra*self.numerador1)
        return numerador_resultado, mcm
        
    def resta():
        pass
    def multiplicar():
        pass
    def dividir():
        pass



 
r = Racional(5, 10 ,6 ,12)
  
print(r.numerador_resultado)

