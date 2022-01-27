ruta='/home/victorjose/'

def lee_fichero(nombre):
    try:
        csv_in = open(nombre)
    except Exception as e:
        print(f'Error al abrir el archivo:{type(e).__name__}')
    else:
        datos = csv_in.read()
        print(datos) 
    

lee_fichero('hola.txt')

def lee_fihcero_2(nombre):
    try:
        pass
    except FileNotFoundError as e:
        print(f'Error al abrir el archivo:{type(e).__name__}')
        print(e)

lee_fihcero_2('')

