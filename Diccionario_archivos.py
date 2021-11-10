from pprint import pprint
ruta = 'funciones_lista.txt'

listas = open(ruta)
lineas = listas.readline()



def diccionary():
    diccionario_total = {}

    for lineas in listas:
        if lineas == ' ':
            break
        archivos = lineas.split(',')
        diccionario_total = {archivos}
        

    return diccionario_total


pprint(diccionary())



# print(ruta)