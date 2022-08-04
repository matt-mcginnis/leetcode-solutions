import unittest
from Solution import Solution

class TestRomanToInt(unittest.TestCase):
    def test_1(self):
        expected = 3
        sol = Solution()
        actual = sol.romanToInt('III')
        self.assertEqual(expected, actual)
    def test_2(self):
        expected = 58
        sol = Solution()
        actual = sol.romanToInt('LVIII')
        self.assertEqual(expected, actual)
    def test_3(self):
        expected = 1994
        sol = Solution()
        actual = sol.romanToInt('MCMXCIV')
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()