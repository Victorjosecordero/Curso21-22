import os
from pprint import pprint

os.system('clear')

ruta = '/home/victorjose/Desktop/VSCODE/codigo/Git/Curso21-22/listas/funciones_lista.txt'
dict_salida = {}



#leer archivos
def modo1():
    clave = 0

    with open(ruta) as archivo:
        for l in archivo:
            fila = l[:-1:].split(',')
            for nombre in fila:
                dict_salida[clave] = nombre
                clave += 1
    pprint(dict_salida)


def modo2():
    clave = 0
    texto = open(ruta,'r').readlines()
    for l1 in texto:
        fila = l1.split(',')
        for arc in fila:
            dict_salida[clave] = arc
            clave += 1
            
    return dict_salida


pprint(modo2())