import os
import pprint
class Personajes():
    atributo = None
    raza = None
    skill1 = None
    skill2 = None
    ulti = None

os.system('clear')
ds7 = Personajes()
ds7.atributo = 'Verde'
ds7.raza = 'Desconocido'
ds7.skill1 = 'Quitar orbes'
ds7.skill2 = 'Rank up'
ds7.ulti = 'Quitar orbes'

print(f'Atributo:{ds7.atributo}')
print(f'Raza:{ds7.raza}')
print(f'Skill 1: {ds7.skill1}')
print(f'Skill 2: {ds7.skill2}')
print(f'Ultimate: {ds7.ulti}')
