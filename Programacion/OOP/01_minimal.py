import os
import pprint
class Coche():
    matricula = None
    num_puertas = None
    color = None


os.system('clear')
bmw = Coche()
bmw.color = 'Verde'
bmw.matricula = '1234-jio'
bmw.num_puertas = 2
bmw.precio = 20000
bmw.marca = 'BMW'
bmw.modelo = 'Panda'

print(f'Color:{bmw.color}')
print(f'Nº de puertas:{bmw.num_puertas}')
print(f'Nº matricula: {bmw.matricula}')
print(f'Precio: {bmw.precio}')
pprint.pprint(dir(bmw))
pprint.pprint(bmw.__class__)
pprint.pprint(bmw.__dict__)