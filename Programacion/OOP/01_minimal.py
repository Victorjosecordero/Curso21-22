import os
import pprint
class Coche():
    matricula = None
    num_puertas = None
    color = None
    motor_en_marcha = False

    def __init__(self, matr, puertas, col):
        self.matricula = matr
        self.num_puertas = puertas
        self.color = col

    def __str__(self) -> str:
        return f'Matricula: {self.matricula} \n Número de puertas: {self.num_puertas}'


    def arrancar(self):
        self.motor_en_marcha = True
    def apagar(self):
        self.motor_en_marcha = False


os.system('clear')
<<<<<<< HEAD
bmw = Coche('9090-klk',3,'azul')
bmw.arrancar()
print('Motor:', bmw.motor_en_marcha)
bmw.color = 'Verde'
bmw.matricula = '1234-jio'
bmw.num_puertas = 2
bmw.precio = 20000
bmw.marca = 'BMW'
bmw.modelo = 'Panda'
bmw.apagar()


print(f'Color:{bmw.color}')
print(f'Nº de puertas:{bmw.num_puertas}')
print(f'Nº matricula: {bmw.matricula}')
print(f'Precio: {bmw.precio}')
# pprint.pprint(dir(bmw))
# pprint.pprint(bmw.__class__)
# pprint.pprint(bmw.__dict__)
print(bmw)
print('Motor:', bmw.motor_en_marcha)
=======
ds7 = Coche()
ds7.color = 'Verde'
ds7.matricula = '1234-jio'
ds7.num_puertas = 2
ds7.precio = 20000
ds7.marca = 'ds7'
ds7.modelo = 'Panda'

print(f'Color:{ds7.color}')
print(f'Nº de puertas:{ds7.num_puertas}')
print(f'Nº matricula: {ds7.matricula}')
print(f'Precio: {ds7.precio}')
pprint.pprint(dir(ds7))
pprint.pprint(ds7.__class__)
pprint.pprint(ds7.__dict__)
>>>>>>> d16c37f99c9b8503a34da0958f67561acd6d81dc
