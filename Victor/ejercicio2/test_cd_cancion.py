#Victor Jose Peña Cordero
import unittest
from cd_cancion import CD, Cancion

class TestClaseCD(unittest.TestCase):

    def test_constructor_por_defecto_crea_lista_vacia(self):
        cd = CD()
        resp = cd.numeroCanciones
        self.assertEqual(resp, 0)

    def test_CD_añade_canciones(self):
        c1= Cancion('a')
        c2 = Cancion('b')
        c3 = Cancion('c')
        cd = CD([c1, c2, c3])
        resp = cd.nomb_cancion(1).nombre_cancion , cd.nomb_cancion(2).nombre_cancion , cd.nomb_cancion(3).nombre_cancion
        self.assertEqual(resp, ('a' , 'b' , 'c'))