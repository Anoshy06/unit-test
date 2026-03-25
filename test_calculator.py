import unittest
from Calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.cal = Calculator()   # reuse object

    def test_add(self):
        self.assertEqual(self.cal.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.cal.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.cal.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.cal.divide(4, 2), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.cal.divide(5, 0)


if __name__ == "__main__":
    unittest.main()