class Gestion_csv():
    __ruta_origen = ''
    __ruta_destino = ''
    fichero_origen = ''
    fichero_destino = ''

    def __init__(self,origen=None,destino=None) -> None:
        self.fichero_origen = origen
        self.fichero_destino = destino
    def leer(self):
        pass
    def escribir(self,contenido):
        pass
    def cerrar(self):
        pass



f = Gestion_csv(origen,destino)
contenido = f.leer()
f.escribir(contenido)