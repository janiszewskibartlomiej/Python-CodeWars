import unittest
from Solution_SortandStar import two_sort

class Test_SortAndStar(unittest.TestCase):
    def test1(self):
        self.assertEquals(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]),
                           'b***i***t***c***o***i***n')
    def test2(self):
        self.assertEquals(two_sort(
            ["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]),
                           'a***r***e')
        self.assertEquals(two_sort(["lets", "talk", "about", "javascript", "the", "best", "language"]),
                           'a***b***o***u***t')
        self.assertEquals(two_sort(["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]),
                           'c***o***d***e')
        self.assertEquals(two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]),
                           'L***e***t***s')

if __name__ == '__main__':
    unittest.main()