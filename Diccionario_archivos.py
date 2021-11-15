from pprint import pprint
ruta = 'funciones_lista.txt'

listas = open(ruta)
lineas = listas.readline()



def diccionary():
    diccionario_total = {}

    for lineas in listas:

        archivos = lineas.split(',')
        diccionario_total = {archivos}
        dict(archivos)
        

    return diccionario_total


pprint(diccionary())


