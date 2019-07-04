import unittest
from solution import toJadenCase

class TestCapitalizing(unittest.TestCase):
    def test_result(self):
        quote = "How can mirrors be real if our eyes aren't real"
        #result = "How Can Mirrors Be Real If Our Eyes Aren't Real"
        self.assertEqual(toJadenCase((quote)), "How Can Mirrors Be Real If Our Eyes Aren't Real")

if __name__ == '__main__':
    unittest.main()