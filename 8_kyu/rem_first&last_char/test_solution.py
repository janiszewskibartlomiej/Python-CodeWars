
import unittest
from solution import remove_char


class TestChampion(unittest.TestCase):
    def test_result_1(self):
        self.assertEqual(remove_char('eloquent', 'loquen')
    def test_result_2(self):
        self.assertEqual(remove_char('country', 'ountr')
    def test_result_3(self):
        self.assertEqual(remove_char('person', 'erso')
    def test_result_4(self):
        self.assertEqual(remove_char('place', 'lac')
    def test_result_5(self):
        self.assertEqual(remove_char('ok'), '')
        
if __name__ == '__main__':
    unittest.main()
