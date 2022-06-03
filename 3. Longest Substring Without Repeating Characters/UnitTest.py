import unittest
from Solution import Solution

class TestLongestSubstringNoRepeats(unittest.TestCase):
    def test_1(self):
        s = 'abcabcbb'
        expected = 3
        actual = Solution.lengthOfLongestSubstring(self, s)
        self.assertEqual(expected, actual)
    def test_2(self):
        s = 'bbbbb'
        expected = 1
        actual = Solution.lengthOfLongestSubstring(self, s)
        self.assertEqual(expected, actual)
    def test_3(self):
        s = 'pwwkew'
        expected = 3
        actual = Solution.lengthOfLongestSubstring(self, s)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
