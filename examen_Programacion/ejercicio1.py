
#Victor José Peña Cordero
import pprint

def leer():
    lista_palabras = []
    with open('examen_Programacion/palabras.txt.TXT') as palabras:
        filas = palabras.readlines()
        for f in filas:
            if int(f.find('e')) == int(-1):
                lista_palabras.append(f[:-1:])
                


    return(lista_palabras)
    

pprint.pprint(leer())

