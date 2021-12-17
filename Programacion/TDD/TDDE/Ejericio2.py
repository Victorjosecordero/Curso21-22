class Raton():
    __posicion_x = None
    __posicion_y = None
    __boton_izquierdo = None
    __boton_derecho = None


    def __init__(self, posicion_x, posicion_y, boton_izquierdo,boton_derecho) -> None:
        self.__posicion_x = posicion_x
        self.__posicion_y = posicion_y
        self.__boton_izquierdo = boton_izquierdo
        self.__boton_derecho = boton_derecho

    def set_posicion_x(self):
        return self.__posicion_x
    def set_posicion_y(self):
        return self.__posicion_y
    def set_boton_izquierdo(self):
        return self.__boton_izquierdo
    def set_boton_derecho(self):
        return self.__boton_derecho

    def get_posicion_x(self):
        return self.__posicion_x
    def get_posicion_y(self):
        return self.__posicion_y
    def get_boton_izquierdo(self):
        return self.__boton_izquierdo
    def get_boton_derecho(self):
        return self.__boton_derecho

    
    def hacer_click():
        pass
    def doble_click():
        pass
    def mover():
        pass
