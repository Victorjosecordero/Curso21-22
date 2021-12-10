
class Pajaro():
    def cantar(self):
        print('Los pájaros tienen cantos diferentes')
    def __getitem__(self,items):
        print(type(items),items)


class Gorrion(Pajaro):
    def cantar(self, con_padre=False):
        if con_padre:
            super().cantar()
        print('Gorrión pio, pio')


class Gallo(Pajaro):
    def cantar(self,con_padre=False):
        if con_padre:
            super().cantar()
        print('Gallo kikirikíiii')


# g = Gorrion()
# g.cantar()

# gallo = Gallo()
# gallo.cantar(True)

class CoroPajaros():
    def __init__(self, lista_pajaros) -> None:
        self.coro = lista_pajaros

    def cantar(self):
        titulo = True
        for p in self.coro:
            p.cantar(titulo)
            titulo = False
    def supervisar(self,lista):
        listado = []
        salida = list()
        for i in lista:
            listado.append(type(i))
        print(listado)
        for i in range(len(lista)):
            if type(lista[i]) in listado:
                salida.append(lista[i])
        print(salida)


    
        # for p in range(len(self.coro)):
        #     if p == 0:
        #         self.coro[p].cantar(True)
        #     else:
        #         self.coro[p].cantar()



# lista_pajaros = ['p',1,'l'] 
b = ['l',Gallo(),Gorrion()]
# p = CoroPajaros(lista_pajaros)
# p.cantar()
paj = Pajaro()
print(paj.__getitem__())
c = CoroPajaros(b)
c.supervisar(b)