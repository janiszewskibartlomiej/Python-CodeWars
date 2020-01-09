import unittest
from SolutionExtractDomain import domain_name

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(domain_name("http://google.com"), "google")
    def test2(self):
        self.assertEqual(domain_name("http://google.co.jp"), "google")
    def test3(self):
        self.assertEqual(domain_name("www.xakep.ru"), "xakep")
    def test4(self):
        self.assertEqual(domain_name("https://youtube.com"), "youtube")

if __name__ == '__main__':
    unittest.main()