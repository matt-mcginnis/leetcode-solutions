import unittest
from Solution import Solution, ListNode

class TestAddTwoNumbers(unittest.TestCase):
    def test_1(self):
        l1 = ListNode(2, ListNode(4, ListNode(3, None)))
        l2 = ListNode(5, ListNode(6, ListNode(4, None)))
        expected = ListNode(7, ListNode(10, ListNode(7, None)))
        sol = Solution()
        actual = sol.addTwoNumbers(l1, l2)
        while actual or expected:
            exp = expected.val if expected else None
            act = actual.val if actual else None
            self.assertEqual(exp, act)
            expected = expected.next if expected else None
            actual = actual.next if actual else None
    def test_2(self):
        l1 = ListNode(0, None)
        l2 = ListNode(0, None)
        expected = ListNode(0, None)
        sol = Solution()
        actual = sol.addTwoNumbers(l1, l2)
        while actual or expected:
            exp = expected.val if expected else None
            act = actual.val if actual else None
            self.assertEqual(exp, act)
            expected = expected.next if expected else None
            actual = actual.next if actual else None
    def test_3(self):
        l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))
        l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))
        expected = ListNode(18, ListNode(18, ListNode(18, ListNode(18, ListNode(9, ListNode(9, ListNode(9, None)))))))
        sol = Solution()
        actual = sol.addTwoNumbers(l1, l2)
        while actual or expected:
            exp = expected.val if expected else None
            act = actual.val if actual else None
            self.assertEqual(exp, act)
            expected = expected.next if expected else None
            actual = actual.next if actual else None

if __name__ == "__main__":
    unittest.main()
