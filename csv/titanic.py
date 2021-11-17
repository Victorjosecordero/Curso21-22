
import pandas as pd


ruta = "/home/victorjose/Desktop/VSCODE/codigo/Git/Curso21-22/csv/"


def contador():
    df = pd.read_csv(ruta + 'titanic.csv')
    survived = df['Survived']

    vivos = 0

    muertos = 0

    for s in survived:
        if s == 1:
            vivos += 1
        else:
            muertos += 1
    return vivos,muertos

v,m = contador()

print('Vivieron:')
print(v)
print('Murieron:')
print(m)