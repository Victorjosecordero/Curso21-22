import os
from settings import MI_CARPETA, RUTA_BASE, VSCODE

os.system('clear')

actual = os.getcwd()
print(actual)

nuevo_dir = os.chdir(RUTA_BASE)
actual = os.getcwd()
print(actual)
print('-'*50)
archivos = os.scandir(RUTA_BASE + VSCODE)
for a in archivos:
    if a.is_dir():
        print(a.name)

ruta_salida = RUTA_BASE + VSCODE + MI_CARPETA
if not os.path.exists(ruta_salida):
    os.makedirs(ruta_salida)


nuevo = open(ruta_salida + '/mi_archivo.txt','w')
nuevo.write('Hola Mundo')
nuevo.close()
print()