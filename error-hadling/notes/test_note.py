import unittest
from main import promedio


class TestPromedio(unittest.TestCase):

    def test_promedio_valido(self):
        self.assertEqual(promedio([4, 5, 3]), 4.0)

    def test_lista_vacia(self):
        with self.assertRaises(ValueError):
            promedio([])


if __name__ == "__main__":
    unittest.main()
