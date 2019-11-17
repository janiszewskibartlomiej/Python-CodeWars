import unittest
from solutionSortAndStar import two_sort

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEquals(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]),
                           'b***k***m***o***p')
    def test3(self):
        self.assertEquals(two_sort(
            ["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]),
                           'a***b***c***e***r***w')
    def test3(self):
        self.assertEquals(two_sort(["lets", "talk", "about", "javascript", "the", "best", "language"]),
                           'a***b***j')
    def test4(self):
        self.assertEquals(two_sort(["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]),
                           'c***d***i***o')
    def test5(self):
        self.assertEquals(two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]),
                           'L***a***c***g***h***o***s***v')


if __name__ == '__main__':
    unittest.main()
