'''  Jose Manuel Perez Puig
clase para las pruebas unitarias de la clase Curso'''

import unittest
from claseCurso import Curso
from claseAlumno import Alumno

CLASE = 'DAM'
RUTA = '/Users/jmpp/Documents/GitHub/codigo_21-22/Trimestre-2/B03_Ejercicios_Calificaciones-CD_Libros/'
ARCHIVO = 'archivo_alumnos.csv'

class TestClaseCurso(unittest.TestCase):
    def test_existencia(self):
        c = Curso(CLASE)
        self.assertNotEqual(c, False)

    def test_constructor_solo_con_nombre_crea_curso_con_nombre_y_lista_vacia(self):
        c = Curso(CLASE)
        resp1 = c.nombre_curso
        resp2 = c.alumnos
        self.assertEqual(resp1, CLASE)
        self.assertEqual(resp2, [])


    def test_constructor_con_nombre_y_lista_alumnos_crea_curso_con_nombre_y_lista_de_obj(self):
        a1 = Alumno(['Marcos', 5, 6, 7, 8, 9, 10])
        a2 = Alumno(['Gabriel', 5, 6, 5, 6.5, 7, 6])
        c = Curso(CLASE,[a1, a2])
        resp1 = c.nombre_curso
        resp2 = c.alumnos
        out = 'Marcos = [5, 6, 7, 8, 9, 10]\nGabriel = [5, 6, 5, 6.5, 7, 6]\n'
        self.assertEqual(resp1, CLASE)
        self.assertEqual(resp2, out)


    def test_constructor_desde_csv_crea_curso_con_nombre_y_lista_de_obj(self):
        c = Curso.desde_csv(CLASE, ARCHIVO)
        resp1 = c.nombre_curso
        resp2 = c.alumnos
        out = 'Marcos = [5, 6, 7, 8, 9, 10]\nGabriel = [5, 6, 5, 6.5, 7, 6]\n'
        self.assertEqual(resp1, CLASE)
        self.assertEqual(resp2, out)

