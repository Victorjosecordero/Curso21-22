import os
import settings

def clear():
    os.system('clear')




def buscar(ruta_de_busqueda, extension='.py'):
    """
    Busca en la carpeta selecionada archivos que acaben en .py y la devuelve en una lista sin .py
    """
    lista_archivos = []
    archivos = os.scandir(ruta_de_busqueda)
    for a in archivos:
        if a.name.endswith(extension):
            lista_archivos.append(a.name[:-3:])
    return  lista_archivos

def agrupar(lista_archivos,miembros):
    """
    Toma una cadena de texto y devulve agrupamientos de esas cadenas
    """
    fila = ''
    for i in range(0,len(lista_archivos),miembros):
        temp = lista_archivos[i: i + miembros]
        fila += ','.join(temp) + '\n'
    return fila


def escribir(cadena,archivo):
    nuevo = open(archivo,'w')
    nuevo.write(cadena)
    nuevo.close


ruta = settings.RUTA_BASE + settings.VSCODE
ruta_salida = settings.RUTA_BASE + settings.VSCODE + settings.MI_CARPETA
clear()
x = buscar(ruta)
f = agrupar(x,5)
escribir(f,ruta_salida + '/funciones_lista.txt')