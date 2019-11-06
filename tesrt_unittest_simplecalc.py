from simple_cal import simple_cal
import unittest

class CalcTests(unittest.TestCase):

    calc = simple_cal()


    def test_add (self):
        self.assertEqual(self.calc.add(3,  2),  5)
    def test_sub(self):
        self.assertEqual(self.calc.subtract(3,3), 0)
    def test_mult(self):
        self.assertEqual(self.calc.mult(3,  4),  12)

if __name__=='__main__':
    unittest.main()