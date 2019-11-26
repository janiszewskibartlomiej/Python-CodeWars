import unittest
from solutionBonus import bonus_time

class TestBonus(unittest.TestCase):
    def test1(self):
        self.assertEquals(bonus_time(10000, True), '$100000')
    def test2(self):
        self.assertEquals(bonus_time(25000, True), '$250000')
    def test3(self):
        self.assertEquals(bonus_time(10000, False), '$10000')
    def test4(self):
        self.assertEquals(bonus_time(60000, False), '$60000')
    def test5(self):
        self.assertEquals(bonus_time(2, True), '$20')
    def test6(self):
        self.assertEquals(bonus_time(78, False), '$78')
    def test7(self):
        self.assertEquals(bonus_time(67890, True), '$678900')

if __name__ == '__main__':
    unittest.main()