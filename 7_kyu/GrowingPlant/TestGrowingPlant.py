import unittest
from SolutionGrowingPlant import growing_plant


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEquals(growing_plant(100,10,910),10)
        self.assertEquals(growing_plant(10,9,4),1)
        self.assertEquals(growing_plant(5,2,0),1)
        self.assertEquals(growing_plant(5,2,5),1)
        self.assertEquals(growing_plant(5,2,6),2)


if __name__ == '__main__':
    unittest.main()
