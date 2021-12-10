import os
import csv

class Generador():
    __esqueleto = """ 
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            ###_###
        </body>
        </html>"""
    def __generar_esqueleto(self):
        return self.__esqueleto

    def __generar_tabla(self):
        if self.__lista:
            tabla = '<table><tr>'
            cabecera = lidt(self.__lista[0].keys)
            for c in cabecera:
                tabla += f'<td>{c}</td>'
            tabla += '</tr>'
        return tabla
        

    def generar_pagina(self,lista):
        self.__lista = lista
        if not lista:
            return self.__generar_esqueleto()
        else:
            pag = self.__generar_tabla
            print(pag)

def leer_dict():
    csv_in = open('/home/victorjose/Github/Curso21-22/Programacion/Generador/titanic.csv')
    lector_dict = csv.DictReader(csv_in)
    lista_dict = list(lector_dict)
    csv_in.close()
    return lista_dict


elementos = leer_dict()
g = Generador(elementos)
pagina = g.generar_pagina(elementos)