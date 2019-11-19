import unittest
from solution_BMI import bmi

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEquals(bmi(50, 1.80), "Underweight")
    def test2(self):
        self.assertEquals(bmi(80, 1.80), "Normal")
    def test3(self):
        self.assertEquals(bmi(90, 1.80), "Overweight")
    def test4(self):
        self.assertEquals(bmi(110, 1.80), "Obese")
    def test5(self):
        self.assertEquals(bmi(50, 1.50), "Normal")


if __name__ == '__main__':
    unittest.main()
