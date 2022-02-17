'''  Jose Manuel Perez Puig
clase para las pruebas unitarias de la clase ListaLibros'''

import unittest
from claseListaLibros import ListaLibros

class TestClaseListaLibros(unittest.TestCase):
    def test_existencia(self):
        biblio = ListaLibros()
        self.assertNotEqual(biblio, False)

    def test_constructor_por_defecto_crea_lista_vacia(self):
        biblio = ListaLibros()
        resp = biblio.numero_de_libros
        self.assertEqual(resp, 0)

    def test_constructor_con_lista_de_libros_crea_ListaLibros_con_esos_libros_en_orden_alfabetico(self):
        l1 = 'La isla del tesoro'
        l2 = 'El asesinato de Pitágoras'
        l3 = 'Amanecer rojo'
        l4 = 'El topo'
        biblio = ListaLibros([l1, l2, l3, l4])
        resp1 = biblio.numero_de_libros
        resp2 = biblio.__str__()
        out = '\n*** 4 Libros actualmente en la Lista:\n    --------------------------------\n    n.1 - Amanecer rojo\n    n.2 - El asesinato de Pitágoras\n    n.3 - El topo\n    n.4 - La isla del tesoro\n'
        self.assertEqual(resp1, 4)
        self.assertEqual(resp2, out)

    def test_insertar_libro_en_la_listaLibros_según_orden_alfabetico(self):
        l1 = 'La isla del tesoro'
        l2 = 'El asesinato de Pitágoras'
        l3 = 'Amanecer rojo'
        l4 = 'El topo'
        biblio = ListaLibros([l1, l2, l3, l4])
        biblio.inserta_libro('Cosmos')
        resp1 = biblio.numero_de_libros
        resp2 = biblio.obtener_libro(2)
        self.assertEqual(resp1, 5)
        self.assertEqual(resp2, 'Cosmos')

    def test_eliminar_libro_dada_posicion_valida_en_ListaLibros_decrece_ListaLibros(self):
        l1 = 'La isla del tesoro'
        l2 = 'El asesinato de Pitágoras'
        l3 = 'Amanecer rojo'
        l4 = 'El topo'
        biblio = ListaLibros([l1, l2, l3, l4])
        biblio.elimina_libro(1)
        resp1 = biblio.numero_de_libros
        resp2 = biblio.__str__()
        out = '\n*** 3 Libros actualmente en la Lista:\n    --------------------------------\n    n.1 - El asesinato de Pitágoras\n    n.2 - El topo\n    n.3 - La isla del tesoro\n'
        self.assertEqual(resp1, 3)
        self.assertEqual(resp2, out)

    def test_eliminar_libro_dada_posicion_fuera_de_rango_en_ListaLibros_da_mensaje_de_error_al_usuario(self):
        l1 = 'El topo'
        l2 = 'Amanecer rojo'
        biblio = ListaLibros([l1, l2])
        resp1 = biblio.numero_de_libros
        resp2 = biblio.__str__()
        out = '\n*** 2 Libros actualmente en la Lista:\n    --------------------------------\n    n.1 - Amanecer rojo\n    n.2 - El topo\n'
        self.assertEqual(biblio.elimina_libro(3), None)
        self.assertEqual(resp1, 2)
        self.assertEqual(resp2, out)