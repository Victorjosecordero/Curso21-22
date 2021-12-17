import unittest
import examen

class TestExamen1(unittest.TestCase):
    def test_sumar_no_argumentos_da_error(self):
        respuesta = examen.sumar([])
        self.assertEqual(respuesta,"Error: No hay argumentos")
    def test_sumar_prueba_sumar_enteros_y_float(self):
        respuesta = examen.sumar([6,7,3,1])
        self.assertEqual(respuesta,17)
    def test_sumar_no_falla_si_pasan_cadenas(self):
        respuesta = examen.sumar("holamundo")
        self.assertEqual(respuesta,0)
    def test_sumar_datos_complejos_es_0(self):
        respuesta = examen.sumar((21,"holamundo",1998))
        self.assertEqual(respuesta,0)
    def test_sumar_objetos_no_numerico_es_0(self):
        respuesta = examen.sumar("a,b")
        self.assertEqual(respuesta,0)