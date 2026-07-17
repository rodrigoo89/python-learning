import unittest
import cambia_texto

class TestCambiaTexto(unittest.TestCase):
    def test_todo_mayusculas(self):
        self.assertEqual(cambia_texto.todo_mayusculas("hola"), "HOLA")
        self.assertEqual(cambia_texto.todo_mayusculas("Python"), "PYTHON")
        self.assertEqual(cambia_texto.todo_mayusculas("123abc"), "123ABC")

if __name__ == '__main__':
    unittest.main()