

class Pajaro():
    def cantar(self):
        print('Los pájaros tienen cantos diferentes')


class Gorrion(Pajaro):
    def cantar(self,con_padre=False):
        if con_padre:
            super().cantar()
        print('Gorrion pio, pio')

class Gallo(Pajaro):
    def cantar(self,con_padre=False):
        if con_padre:
            super().cantar()
        print('Gallo kikiriquíi')


# g = Gorrion()
# g.cantar()
# gallo = Gallo()
# gallo.cantar()

class CoroPrajaros():
    coro = [Gorrion(),Gallo()]
    def cantar(self):
        titulo = True
        for p in self.coro:
            p.cantar(titulo)
            titulo = False
        # for p in range(len(self.coro)):
        #     if p == 0:
        #         self.coro[p].cantar(True)
        #     else:
        #         self.coro[p].cantar()


g = Gallo
c.cantar()

type(super(g))