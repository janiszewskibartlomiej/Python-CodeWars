import unittest
from solution import points


class TestChampion(unittest.TestCase):
    def test_result_1(self):
        self.assertEqual(points((['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3'])), 30)
    def test_result_2(self):
        self.assertEqual(points((['1:1', '2:2', '3:3', '4:4', '2:2', '3:3', '4:4', '3:3', '4:4', '4:4'])), 10)
    def test_result_3(self):
        self.assertEqual(points((['0:1', '0:2', '0:3', '0:4', '1:2', '1:3', '1:4', '2:3', '2:4', '3:4'])), 0)
    def test_result_4(self):
        self.assertEqual(points((['1:0', '2:0', '3:0', '4:0', '2:1', '1:3', '1:4', '2:3', '2:4', '3:4'])), 15)
    def test_result_5(self):
        self.assertEqual(points((['1:0', '2:0', '3:0', '4:4', '2:2', '3:3', '1:4', '2:3', '2:4', '3:4'])), 12)


if __name__ == '__main__':
    unittest.main()
