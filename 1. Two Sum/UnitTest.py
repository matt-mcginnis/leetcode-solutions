import unittest
from Solution import Solution

class TestTwoSum(unittest.TestCase):
    def test_1(self):
        nums = [2,7,11,15]
        target = 9
        expected = [0,1]
        actual = Solution.twoSum(self, nums, target)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()