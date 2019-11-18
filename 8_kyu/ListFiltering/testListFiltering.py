import unittest
from SolutionListFiltering import filter_list

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEquals(filter_list([1,2,'a','b']),[1,2])
    def test2(self):
        self.assertEquals(filter_list([1,'a','b',0,15]),[1,0,15])
    def test3(self):
        self.assertEquals(filter_list([1,2,'aasf','1','123',123]),[1,2,123])


if __name__ == '__main__':
    unittest.main()
