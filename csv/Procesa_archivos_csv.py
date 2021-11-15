import os
import csv
import pprint

ruta = '/home/victorjose/Desktop/VSCODE/codigo/Git/Curso21-22/csv/'
def leer_csv_normal():
    with open(ruta + 'archivos.csv') as csv_in:
        filas = csv_in.readlines()
        for f in filas:
            print(f[:-1:].split(','))

# leer_csv_normal()

def leer_con_csv():
    campos = []
    filas = []

    csv_in = open(ruta + 'archivos.csv')
    lector = csv.reader(csv_in)
    campos = next(lector)

    for f in lector:
        filas.append(f)
    
    csv_in.close()
    return campos,filas

# c,f = leer_con_csv()
# pprint.pprint(c)
# pprint.pprint(f)

def leer_with():
    filas = []
    campos = []

    with open(ruta + 'archivos.csv') as csv_in:
        lector = csv.reader(csv_in)
        for f in lector:
            filas.append(f)
    return campos,filas

# c,f = leer_with()
# pprint.pprint(c)
# pprint.pprint(f)

def leer_dict():
    csv_in = open(ruta + 'New-Zealand-and-district-health-board-period-life-tables-2017-2019-by-NZDep2018-CSV.csv')
    lector_dict = csv.DictReader(csv_in)

    lista_dict = list(lector_dict)

    csv_in.close()

    return lista_dict

pprint.piprint(leer_dict())