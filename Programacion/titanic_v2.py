

import os
import csv

os.system('clear')
ruta = "/home/victorjose/Github/Curso21-22/Programacion/csv/"


def leer_dict():
    csv_in = open(ruta + 'titanic.csv')
    lector_dict = csv.DictReader(csv_in)

    lista_dict = list(lector_dict)

    csv_in.close()

    return lista_dict


lista_dicionario = leer_dict()
def imprimir():
    for i in lista_dicionario:
        if i['Age'] >= '20' and i['Age'] <= '30' and i['Survived'] == '1':
            # print(f'Nombre: {i["Name"]}')
            # print(f'Clase: {i["Pclass"]}')
            # print(f'Sexo: {i["Sex"]}')
             with open(ruta + 'titanic_nombres','a') as csv_writer:
                escribir = csv.writer(csv_writer)
                escribir.writerow([f'Nombre: {i["Name"]}'])
                escribir.writerow([f'Clase: {i["Pclass"]}'])
                escribir.writerow([f'Sexo: {i["Sex"]}'])
        else:
            pass

    return 

imprimir()