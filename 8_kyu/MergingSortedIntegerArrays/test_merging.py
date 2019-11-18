import unittest
from solutionMergingSortedIntigerArrays import merge_arrays

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEquals(merge_arrays([1, 3, 5], [2, 4, 6]), ([1, 2, 3, 4, 5, 6]))
        self.assertEquals(merge_arrays([2, 4, 8], [2, 4, 6]), ([2, 4, 6, 8]))


if __name__ == '__main__':
    unittest.main()
