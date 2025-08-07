# test_calculator.py

import unittest
from your_module_name import SimpleCalculator  # Replace 'your_module_name' with the name of your .py file

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertIsNone(self.calc.divide(10, 0))

if __name__ == '__main__':
    unittest.main()
