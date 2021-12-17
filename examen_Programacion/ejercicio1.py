
#Victor José Peña Cordero


def leer():
    lista_palabras = []
    with open('examen_Programacion/palabras.txt.TXT') as palabras:
        filas = palabras.readlines()
        for f in filas:
            if int(f.find('e')) == int(-1):
                pass
            else:
                lista_palabras.append(f)


    print(lista_palabras)
    

leer()

