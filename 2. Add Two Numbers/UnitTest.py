import unittest
from Solution import Solution, ListNode

class TestAddTwoNumbers(unittest.TestCase):
    def test_1(self):
        l1 = ListNode(2, ListNode(4, ListNode(3, None)))
        l2 = ListNode(5, ListNode(6, ListNode(4, None)))
        expected = ListNode(7, ListNode(0, ListNode(8, None)))
        actual = Solution.addTwoNumbers(self, l1, l2)
        while actual or expected:
            self.assertEqual(expected.val, actual.val)
            expected = expected.next
            actual = actual.next
    def test_2(self):
        l1 = ListNode(0, None)
        l2 = ListNode(0, None)
        expected = ListNode(0, None)
        actual = Solution.addTwoNumbers(self, l1, l2)
        while actual or expected:
            self.assertEqual(expected.val, actual.val)
            expected = expected.next
            actual = actual.next
    def test_3(self):
        l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))
        l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))
        expected = ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1, None))))))))
        actual = Solution.addTwoNumbers(self, l1, l2)
        while actual or expected:
            self.assertEqual(expected.val, actual.val)
            expected = expected.next
            actual = actual.next
if __name__ == "__main__":
    unittest.main()
