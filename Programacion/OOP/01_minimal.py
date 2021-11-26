import os
import pprint
class Coche():
    matricula = None
    num_puertas = None
    color = None


os.system('clear')
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