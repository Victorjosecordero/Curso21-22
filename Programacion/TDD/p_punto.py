class Punto():
    #3
    x = 0
    y = 0
    def __init__(self,x ,y) -> None:
        self.x = x
        self.y = y

    def set_x(self,valor):
        pass

class Rectangulo():
    v1, v2, v3, v4 = Punto(0,0)
    def __init__(self,p1,p2) -> None:
        self.v1 = p1
        self.v2 = p2
        self.v3 = Punto(p1.x,p2.y)
        self.v4 = Punto(p1.y,p2.x)