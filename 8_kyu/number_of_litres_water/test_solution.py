import unittest
from solution_litres import litres

class TestLiters(unittest.TestCase):
    def test1(self):
        self.assertEquals(litres(2), 1,'should return 1 litre');
    def test2(self):
        self.assertEquals(litres(1.4), 0, 'should return 0 litres');
    def test3(self):
        self.assertEquals(litres(12.3), 6, 'should return 6 litres');
    def test4(self):
        self.assertEquals(litres(0.82), 0, 'should return 0 litres');
    def test5(self):
        self.assertEquals(litres(11.8), 5, 'should return 5 litres');
    def test6(self):
        self.assertEquals(litres(1787), 893, 'should return 893 litres');
    def test7(self):
        self.assertEquals(litres(0), 0, 'should return 0 litres');


if __name__ == '__main__':
    unittest.main()
