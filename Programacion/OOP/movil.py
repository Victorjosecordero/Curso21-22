import os

class Movil():
    marca = None
    modelo = None
    color = None
    alto = None
    ancho = None
    peso = None
    so = None
    camara = None

    def encender(self):
        self.estado = True
    def apagar(self):
        self.estado = False
    def reiniciar(self):
        self.apagar()
        self.encender()
    def modo_avion(self):
        pass
    def llamar(self):
        pass
    def recibir_llamadas(self):
        pass

os.system('clear')

redmi = Movil()
redmi.encender()
print('Estado:', redmi.estado)
redmi.marca = 'Xiaomi'
redmi.modelo ='Redmi 9'
redmi.color = 'Azul'
redmi.alto ='163 mm'
redmi.ancho ='77 mm'
redmi.peso = '198 g'
redmi.so ='Android 10/MIUI 11'
redmi.camara ='Si'
redmi.apagar()
print('Estado:',redmi.estado)


print(f'Marca:{redmi.marca}')
print(f'Modelo:{redmi.modelo}')
print(f'Color:{redmi.color}')
print(f'Alto:{redmi.alto}')
print(f'Ancho:{redmi.ancho}')
print(f'Peso: {redmi.peso}')
print(f'Sistema Operativo:{redmi.so}')
print(f'Camara: {redmi.camara}')