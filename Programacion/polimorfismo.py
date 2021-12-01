class Spain():

    def __str__(self) -> str:
        return 'España'

    def capital(self):
        print('La capital de España es Madrid')
    
    def idioma(self):
        print('El idioma oficial es el castellano')

class Portugal():

    def __str__(self) -> str:
        return 'Portugal'

    def capital(self):
        print('La capital de Portugal es Lisboa')
    
    def idioma(self):
        print('El idioma oficial es el portuges')

class Seychelles():

    def __str__(self) -> str:
        return 'Seychelles'

    def capital(self):
        print('La capital de Seychelles es Victoria')
    
    def idioma(self):
        print('El idioma oficial es el criollo seychellense')


class Aduana():
    def pasar(self,origen,destino):
        print(f'Antes estaba en {origen}')
        print(f'Ahora estoy en {destino}')
        origen.capital()
        origen.idioma()
        print('-------------------')
        destino.capital()
        destino.idioma()
        print('------------------')

esp = Spain()
por = Portugal()
sey = Seychelles()


paises = [esp,por,sey]

aduana = Aduana()

aduana.pasar(esp,sey)
print('*************************************')
aduana.pasar(sey,por)
print('*************************************')
aduana.pasar(por,esp)