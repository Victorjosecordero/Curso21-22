class Gestion_csv():
    __ruta_origen = ''
    __ruta_destino = ''
    fichero_origen = ''
    fichero_destino = ''

    def __init__(self,origen=None,destino=None) -> None:
        pass
    def leer(self):
        pass
    def escribir(self,contenido):
        pass
    def cerrar(self):
        pass



f = Gestion_csv(destino='/home/victorjose/Github/Curso21-22/Programacion/Archivos/archivo.csv')
contenido = f.leer()
f.escribir(contenido)