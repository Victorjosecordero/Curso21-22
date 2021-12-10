class Racional():

    def __init__(self, numerador, denominador):
        self.numerador = int(numerador)
        self.denominador = int(denominador)
        if denominador == 0:
            raise Exception("El denominador no puede ser 0")

    def __str__(self):
        return str(self.numerador) + "/" + str(self.denominador)


    def maximo_comun_divisor(self, a, b):
        temporal = 0
        while b != 0:
            temporal = b
            b = a % b
            a = temporal
        return a

    def minimo_comun_multiplo(self, a, b):
        return (a * b) / self.maximo_comun_divisor(a, b)

    def suma(self, otro):
        mcm = self.minimo_comun_multiplo(self.denominador, otro.denominador)
        diferencia_self = mcm/self.denominador
        diferencia_otro = mcm/otro.denominador
        numerador_resultado = (diferencia_self*self.numerador) + \
            (diferencia_otro*otro.numerador)
        return Racional(numerador_resultado, mcm)

    def resta(self, otro):
        mcm = self.minimo_comun_multiplo(self.denominador, otro.denominador)
        diferencia_self = mcm/self.denominador
        diferencia_otro = mcm/otro.denominador
        numerador_resultado = (diferencia_self*self.numerador) - \
            (diferencia_otro*otro.numerador)
        return Racional(numerador_resultado, mcm)

    def multiplicacion(self,otro):
        numeradortotal = self.numerador * otro.numerador
        denominadortotal = self.denominador * otro.denominador
        return Racional (numeradortotal,denominadortotal)

    def dividir(self,otro):
        numeradortotal = self.numerador * otro.denominador
        denominadortotal = self.denominador * otro.numerador
        return Racional(numeradortotal,denominadortotal)

    
    


r = Racional(6, 0)
r2 = Racional(5, 10)
print(f"{r} + {r2} = {r.suma(r2)}")
print(f"{r} - {r2} = {r.resta(r2)}")
print(f"{r} * {r2} = {r.multiplicacion(r2)}")
print(f"{r} / {r2} = {r.dividir(r2)}")