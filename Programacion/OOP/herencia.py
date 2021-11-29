class Vehiculo():
    marca = None
    _modelo = None
    __num_serie= None
    __estado = 'Parado'
    __velocidad = 0
    def __init__(self,marca,modelo, numero_serie) -> None:
        self.marca = marca
        self._modelo = modelo
        self.__num_serie = numero_serie

    def get_num_serie(self):
        return self.__num_serie

    def get_estado(self):
        if (self.__estado == 'Moviendose'):
            return self.__estado + f'a {self.__velocidad} Km/h'
        else:
            return self.__estado

    def moverse(self,velocidad_inicial):
        self.acelerar(velocidad_inicial)
        print('Acelerando...')
        self.__estado = 'Moviendose'
    def pararse(self,velocidad_final):
        self.desacelerar(velocidad_final)
        print('Parando...')
        self.__estado = 'Parado'
    def acelerar(self, incremento):
        self.__velocidad +=incremento
    def desacelerar(self,incremento):
        self.__velocidad -= incremento


class Coche(Vehiculo):
    __matricula = None
    __numero_ruedas = 4
    def __init__(self,matricula, marca, modelo, numero_serie) -> None:
        super().__init__(marca, modelo, numero_serie)
        self.__matricula = matricula

c = Coche('1234-jkl','Renault','4L','1234KKK')
print(c.get_estado())
print(f'Vehiculo matricula {c.__matricula} marca {c.marca} y modelo {c._modelo}, con numero de serie {c.get_num_serie}')