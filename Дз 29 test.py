import unittest
from main import SetOfIntegers, Number

class TestIntegers(unittest.TestCase):
    def test_sum(self):
        set_of_integers = SetOfIntegers([1, 2, 3, 4, 5])
        self.assertEqual(set_of_integers.sum(), 15)

    def test_average(self):
        set_of_integers = SetOfIntegers([1, 2, 3, 4, 5])
        self.assertEqual(set_of_integers.average(), 3)

    def test_maximum(self):
        set_of_integers = SetOfIntegers([1, 2, 3, 4, 5])
        self.assertEqual(set_of_integers.maximum(), 5)

    def test_minimum(self):
        set_of_integers = SetOfIntegers([1, 2, 3, 4, 5])
        self.assertEqual(set_of_integers.minimum(), 1)

class TestNumber(unittest.TestCase):
    def test_conversion(self):
        number = Number(10)
        self.assertEqual(number.to_octal(), '0o12')
        self.assertEqual(number.to_hexadecimal(), '0xa')
        self.assertEqual(number.to_binary(), '0b1010')

if __name__ == '__main__':
    unittest.main()
