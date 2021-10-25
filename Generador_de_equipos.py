# import random
# def genera_equipos(personas):
#     numero = rd.randrange(len(personas))
#     for i in range(numero//2):
#         for i in range(2):
#             par1 = personas.pop(numero)
#         else:
#             par2 =

import random as rd
def genera_equipos(alumnos):
    personas = alumnos.copy()
    rd.shuffle(personas)
    equipos = []
    numero_equipos = len(personas) // 2
    for i in range(numero_equipos):
        eq = []
        eq.append(personas.pop())
        eq.append(personas.pop())
        equipos.append(eq)
    
    if len(personas) > 0:
        equipos[numero_equipos - 1].append(personas.pop())

    return equipos

alumnos = ['victor','antonio','rafa','raul','alejandro','fernando']
for i in range(5):
    x = genera_equipos(alumnos)
    print(x)