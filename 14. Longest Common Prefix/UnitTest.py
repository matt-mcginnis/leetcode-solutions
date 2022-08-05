import unittest
from Solution import Solution

class TestLongestCommonPrefix(unittest.TestCase):
    def test_1(self):
        expected = 'fl'
        sol = Solution()
        actual = sol.longestCommonPrefix(["flower","flow","flight"])
        self.assertEqual(expected, actual)
    def test_2(self):
        expected = ''
        sol = Solution()
        actual = sol.longestCommonPrefix(["dog","racecar","car"])
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main() 