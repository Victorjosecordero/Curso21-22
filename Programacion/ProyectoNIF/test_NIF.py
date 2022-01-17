
import unittest

from numpy import ndindex
from NIF import Nif

class TestNif(unittest.TestCase):
    def test_clase_existe(self):
        nif = Nif()
        self.assertNotEqual(nif,None)


    def test_contructor_num_cero_letra_blanco(self):
        nif = Nif()
        self.assertEqual(nif.numero,0)
        self.assertEqual(nif.letra,' ')

    def test_numero_calcula_letra(self):
        nif = Nif(20000000)
        self.assertEqual(nif.letra,'M')
        nif = Nif(49034111)
        self.assertEqual(nif.letra,'C')

    def test_numero_setter_calcula_letra(self):
        nif = Nif()
        nif.numero = 20000000
        self.assertEqual(nif.letra,'M')
    
    def test_print_dni(self):
        nif = Nif()
        nif.numero = 20000000
        self.assertEqual(nif.__str__(),'20000000-M')