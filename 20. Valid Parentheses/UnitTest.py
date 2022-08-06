import unittest
from Solution import Solution

class TestIsValid(unittest.TestCase):
    def test_1(self):
        expected = True
        sol = Solution()
        actual = sol.isValid('()')
        self.assertEqual(expected, actual)
    def test_2(self):
        expected = True
        sol = Solution()
        actual = sol.isValid('()[]{}')
        self.assertEqual(expected, actual)
    def test_3(self):
        expected = False
        sol = Solution()
        actual = sol.isValid('(]')
        self.assertEqual(expected, actual)
    def test_4(self):
        expected = False
        sol = Solution()
        actual = sol.isValid('(')
        self.assertEqual(expected, actual)
    def test_5(self):
        expected = False
        sol = Solution()
        actual = sol.isValid(']')
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()