import unittest
from SolutionGrowingPlant import growing_plant


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(growing_plant(100,10,910),10)
    def test2(self):
        self.assertEqual(growing_plant(10,9,4),1)
    def test3(self):
        self.assertEqual(growing_plant(5,2,0),1)
    def test4(self):
        self.assertEqual(growing_plant(5,2,5),1)
    def test5(self):
        self.assertEqual(growing_plant(5,2,6),2)


if __name__ == '__main__':
    unittest.main()
