
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
        if l['Sex'] == 'male':
            hombres.append[l['Survived']]
        else:
           mujeres.append[l['Survived']]
    h_v = hombres.count(1)
    h_m = hombres.count(0)
    m_v = mujeres.count(1)
    m_m = mujeres.count(0)

    return (h_m,h_v,m_v,m_m)
resultado = personas()
print(f'Hombres vivos: {resultado[0]} Hombres muertos: {resultado[1]}')
print(f'Mujeres vivas: {resultado[2]} Mujeres muertas: {resultado[3]}')
