#Victor Jose Peña Cordero

import unittest
from ejercicio2 import Coche

class TestCoche(unittest.TestCase):
    def test_introducir_datos(self):
        c = Coche
        c.marca ='Opel'
        c.modelo ='Corsa'
        c.color ='Blanco'
        c.num_puertas = 5
        c.matricula = '6560-JVP'
        self.assertEqual(c.marca, 'Opel')
        self.assertEqual(c.modelo, 'Corsa')
        self.assertEqual(c.color, 'Blanco')
        self.assertEqual(c.num_puertas, 5)
        self.assertEqual(c.matricula, '6560-JVP')