import unittest
from validacion_contrasenia import valid_form

class testValidForm(unittest.TestCase):
    def test_valid_form(self):
        result = valid_form(
            username = "prueba"
            password = "pruebacontra"
        )
        self.assertTrue(result)
        result = valid_form(
            username = "prueba"
            password = "pruebacontra"
        )
        self.assertFalse(result)