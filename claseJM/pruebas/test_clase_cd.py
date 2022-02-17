'''  Jose Manuel Perez Puig
clase para las pruebas unitarias de la clase CD'''

import unittest
from claseCD import CD, Cancion

class TestClaseCD(unittest.TestCase):
    def test_existencia(self):
        cd = CD()
        self.assertNotEqual(cd, False)

    def test_constructor_por_defecto_crea_lista_vacia(self):
        cd = CD()
        resp = cd.numeroCanciones
        self.assertEqual(resp, 0)

    def test_constructor_con_lista_canciones_crea_CD_con_esas_canciones(self):
        c1 = Cancion('Hoy no me puedo levantar')
        c2 = Cancion('El pistolero ha llegado a la ciudad')
        c3 = Cancion('We will rock you')
        cd = CD([c1, c2, c3])
        resp1 = cd.numeroCanciones
        resp2 = cd.dameCancion(1).nombre_cancion , cd.dameCancion(2).nombre_cancion , cd.dameCancion(3).nombre_cancion
        self.assertEqual(resp1, 3)
        self.assertEqual(resp2, ('Hoy no me puedo levantar' , 'El pistolero ha llegado a la ciudad' , 'We will rock you'))
    
    