import unittest
from Solution import Solution, ListNode

class TestLinkedListIsPalindrome(unittest.TestCase):
    def test_1(self):
        l = ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))
        expected = True
        sol = Solution()
        actual = sol.isPalindrome(l)
        self.assertEqual(expected, actual)
    def test_2(self):
        l = ListNode(1, ListNode(2, None))
        expected = False
        sol = Solution()
        actual = sol.isPalindrome(l)
        self.assertEqual(expected,actual)

if __name__ == "__main__":
    unittest.main()
