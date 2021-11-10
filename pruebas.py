import os
from settings import RUTA_BASE, VSCODE, MI_CARPETA

nombres = []


# def prueba():

#     os.system('clear')

   

#     ruta_salida = RUTA_BASE + VSCODE + MI_CARPETA
#     if not os.path.exists(ruta_salida):
#         os.makedirs(ruta_salida)


#     nuevo = open(ruta_salida + '/mi_archivo.txt','w')
#     nuevo.write(prueba2)
#     nuevo.close()
#     print()
#     return



def prueba2():
    archivos = os.scandir(RUTA_BASE + VSCODE + MI_CARPETA)
    for a in archivos:
            if a.is_file():
                nombres.append(a.name)
                
                
prueba2()