import unittest
import calculadora

class CalculadoraTest(unittest.TestCase):
    def test_caracteres_no_numericos_devuelve_error(self):
        respuesta = calculadora.sumar('a,b')
        self.assertEqual(respuesta,"Error: Carácter no numérico")
    
    def test_cadena_vacia_devuelve_cero(self):
        respuesta = calculadora.sumar('')
        self.assertEqual(respuesta,0)