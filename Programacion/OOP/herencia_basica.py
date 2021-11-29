class Base():
    datos = []



class Hijo1(Base):
    datos = []
    def __init__(self,elemento):
        self.datos.append(elemento)
    def datos_base(self):
        return super().datos



class Hijo2(Base):
    datos = []
    def __init__(self,elemento):
        self.datos.append(elemento)



h1 = Hijo1('Hijo1')
h2 = Hijo2('Hijo2')



print(h1.datos_base())
print(h2)

print(h1.datos)
print(h2.datos)