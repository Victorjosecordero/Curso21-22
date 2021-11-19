import csv
import os

os.system('clear')

ruta ='/home/victorjose/Desktop/VSCODE/codigo/Git/Curso21-22/csv/'





def csv_write():

    matriz = [
        [1,2,5,6,7],
        [9,8,7,5,8],
        [9,2,5,7,3]
    ]

    with open(ruta + 'nuevo_csv','a') as csv_writer:
        escritor = csv.writer(csv_writer)
        escritor.writerow(['jueves']*10 + ['viernes'])
        escritor.writerow(['nada']* 10 + ['fin'])
        escritor.writerows(matriz)

csv_write()