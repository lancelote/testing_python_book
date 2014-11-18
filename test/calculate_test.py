import unittest
import sys
sys.path.append("..")

from app.calculate import Calculate


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculate()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))

if __name__ == '__main__':
    unittest.main()