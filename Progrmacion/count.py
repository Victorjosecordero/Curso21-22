
# import pandas as pd


# ruta = "/home/victorjose/Desktop/VSCODE/codigo/Git/Curso21-22/csv/"


# def contador():
#     df = pd.read_csv(ruta + 'titanic.csv')
#     survived = df['Sex']
    

#     hombres = 0

#     mujeres = 0

#     for s in survived:
#         if s == 'male':
#             hombres += 1
#         else:
#             mujeres += 1
#     return hombres,mujeres

# h,m = contador()

# print(f'Hombres: {h}')
# print(f'Mujeres: {m}')

from mmap import MADV_REMOVE
import pprint
import csv

ruta = "/home/victorjose/Desktop/VSCODE/codigo/Git/Curso21-22/csv/"


def leer_dict():
    csv_in = open(ruta + 'titanic.csv')
    lector_dict = csv.DictReader(csv_in)

    lista_dict = list(lector_dict)

    csv_in.close()

    return lista_dict



def personas():

    lista_dicionario = leer_dict()
    hombres = []
    mujeres = []
    h_v = 0
    h_m = 0
    m_v = 0
    m_m = 0
    for l in lista_dicionario:
        if l['Sex'] == 'male' and l['Survived'] == '1':
            h_v += 1
        if l['Sex'] == 'male' and not l['Survived'] == '0':
            h_m += 1
        if l['Sex'] == 'female' and l['Survived'] == '1':
            m_v += 1
        if l['Sex'] == 'female' and not l['Survived'] == '1':
            m_m += 1

    return (h_m,h_v,m_v,m_m)
resultado = personas()
print(f'Hombres vivos: {resultado[1]} Hombres muertos: {resultado[0]}')
print(f'Mujeres vivas: {resultado[3]} Mujeres muertas: {resultado[2]}')
