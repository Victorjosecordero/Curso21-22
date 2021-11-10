import os
import settings

os.system('clear')

#Buscar los archivos
#Seleccionar los archivos
lista_archivos = []
ruta_salida = settings.RUTA_BASE + settings.VSCODE + settings.MI_CARPETA
miembros = 5
fila = ''

#Procesar nombre de archivos
archivos = os.scandir(settings.RUTA_BASE + settings.VSCODE)
for a in archivos:
    if a.name.endswith('.py'):
    # if not a.is_dir() and not a.name.startswith('.'):
            lista_archivos.append(a.name[:-3:])


# if not os.path.exists(ruta_salida):
#     os.makedirs(ruta_salida)


#Agruparlos de 5 en 5

    nuevo = open(ruta_salida + '/lista_py2.txt','w')
    for i in range(0,len(lista_archivos),miembros):
        temp = lista_archivos[i: i + miembros]
        fila =','.join(temp) + '\n'
    
        nuevo.write(fila)
    
#Guardar archivos en el fichero
    nuevo.close()

