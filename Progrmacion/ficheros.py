from pprint import pp, pprint

archivo = 'listas.py'
listas = open(archivo)
# lineas = listas.readlines()
# for l in lineas:
#     pprint(l)

# listas.close()


for linea in listas:
    pprint(linea)