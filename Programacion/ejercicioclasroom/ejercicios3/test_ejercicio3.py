#Victor Jose Peña Cordero

import unittest
from ejercicio3 import Tiempo

class TestTiempo(unittest.TestCase):
    

    def test_hora_por_defecto(self):
        t = Tiempo()
        self.assertEqual(t.horas,00)
        self.assertEqual(t.minutos, 00)
        self.assertEqual(t.segundos, 00)
    
    def test_tiempo_con_cadenas(self):
        t = Tiempo('15','30','45')
        self.assertEqual(t.horas,15)
        self.assertEqual(t.minutos, 30)
        self.assertEqual(t.segundos, 45)
    def test_tiempo_con_enteros(self):
        t = Tiempo(15,30,45)
        self.assertEqual(t.horas,15)
        self.assertEqual(t.minutos, 30)
        self.assertEqual(t.segundos, 45)

    def test__introducir_hora(self):
        t = Tiempo()
        t.horas = 15
        t.minutos = 30
        t.segundos = 45
        self.assertEqual(t.horas, 15)
        self.assertEqual(t.minutos, 30)
        self.assertEqual(t.segundos, 45)

