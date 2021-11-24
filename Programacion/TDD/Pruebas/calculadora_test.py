import unittest
import calculadora

class CalculadoraTest(unittest.TestCase):
    def test_caracteres_no_numericos_devuelve_errores(self):
        respuesta = calculadora.sumar('a,b')
        self.assertEqual(respuesta,"Error:Caráter no numérico")
