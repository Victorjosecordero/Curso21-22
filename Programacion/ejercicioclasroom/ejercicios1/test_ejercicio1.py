#Victor Jose Peña Cordero

import unittest
from ejercicio1 import Rectangulo

class TestRectangulo(unittest.TestCase):
    def test_area(self):
        sol =Rectangulo.area(1,2,1)
        self.assertEqual(sol,2)
