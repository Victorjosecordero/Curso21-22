from calificaciones import Calificacion
import unittest as ut


class TestCalificacion(ut.TestCase):
    def test_existencia(self):
        cal = Calificacion()
        self.assertNotEqual(cal, None)
    def test_contructor_vacio_propiedad_vacias(self):
        cal = Calificacion()
        self.assertEqual(cal.nombre,'')
        self.assertEqual(cal.notas,[])
    def test_constructor_recibe_valores_establece_props(self):
        cal = Calificacion(['Raul',9.2,5,4,5,7,9.1])
        self.assertEqual(cal.nombre,'Raul')
        self.assertEqual(cal.notas,[9.2,5,4,5,7,9.1])
    def test_metodo_str_devuelve_alumno_calificacion(self):
        cal = Calificacion()
        cadena = cal.__str__()
        self.assertEqual(cadena,'Alumno: Raul tiene la calificacion NOTABLE')

    def test_calcula_calificacion_vacio_devuelve_None(self):
        cal = Calificacion()
        self.assertEqual(cal.calcula_calificacion(), None)
    
    def test_calcula_calificacion_no_vacio_devuelve_calificacion(self):
        cal = Calificacion(['Raul',9.2,5,4,5,7,9.1])
        self.assertEqual(cal.calcula_calificacion(),'Notable')
        self.assertEqual(cal.calificacion,'Notable')


