# Ejercicio 1:
# Programa que pida al usuario los siguientes datos:
# -nombre
# -Apellidos
# -Fecha nacimiento
# -Telefono

# tiene que pedir datos hasta que el usuarui diga que termino-

# los datos se guardan en un dicionario

# al final se muestra el diccionario


import os
import pprint
import csv

os.system('clear')

def infomacion():
    seguir = True
    lista_personas = []

    while seguir:
        nombre = input('Escriba su nombre:')
        apellidos = input('Escriba sus apellidos:')
        fecha_de_nacimiento = input('Escriba su fecha de nacimiento:')
        telefono = input('Escriba su telefono:')
        diccionario = {'Nombre':nombre, 'Apellidos': apellidos, 'Fecha de nacimiento': fecha_de_nacimiento, 'Telefono': telefono}
        
        lista_personas.append(diccionario)
        respuesta = input('¿Quiere seguir metiendo datos? (Y/N):')
   
        if respuesta.upper() == 'Y':
            seguir = False
        os.system('clear')
    return diccionario

pprint.pprint(infomacion())