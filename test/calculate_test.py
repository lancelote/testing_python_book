import unittest
from calculator_app.calculate import Calculate


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculate()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))

    def test_add_method_raises_typeerror_if_not_ints(self):
        self.assertRaises(TypeError, self.calc.add, "Hello", "World")

    def test_subtract_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.subtract(6, 2))
        self.assertEqual(-2, self.calc.subtract(0, 2))

    def test_subtract_method_raises_typeerror_if_not_ints(self):
        self.assertRaises(TypeError, self.calc.subtract, "Hello", "World")

    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(8, self.calc.multiply(4, 2))
        self.assertEqual(0, self.calc.multiply(0, 2))
        self.assertEqual(-4, self.calc.multiply(4, -1))

    def test_multiply_method_raises_typeerror_if_not_ints(self):
        self.assertRaises(TypeError, self.calc.multiply, "Hello", "World")

if __name__ == '__main__':
    unittest.main()