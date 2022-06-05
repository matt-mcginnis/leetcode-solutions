import unittest
from Solution import Solution, ListNode

class TestAddTwoNumbers(unittest.TestCase):
    def test_1(self):
        l1 = ListNode(2, ListNode(4, ListNode(3, None)))
        l2 = ListNode(5, ListNode(6, ListNode(4, None)))
        test_1_sol = Solution()
        expected = ListNode(7, ListNode(0, ListNode(8, None)))
        actual = test_1_sol.addTwoNumbers(l1, l2)
        while actual or expected:
            if (actual and expected):
                self.assertEqual(expected.val, actual.val)
                expected = expected.next
                actual = actual.next
            else:
                self.fail('Unequal Lengths')
    def test_2(self):
        l1 = ListNode(0, None)
        l2 = ListNode(0, None)
        test_2_sol = Solution()
        expected = ListNode(0, None)
        actual = test_2_sol.addTwoNumbers(l1, l2)
        while actual or expected:
            if (actual and expected):
                self.assertEqual(expected.val, actual.val)
                expected = expected.next
                actual = actual.next
            else:
                self.fail('Unequal Lengths')
    def test_3(self):
        l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))
        l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))
        test_3_sol = Solution()
        expected = ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1, None))))))))
        actual = test_3_sol.addTwoNumbers(l1, l2)
        while actual or expected:
            if (actual and expected):
                self.assertEqual(expected.val, actual.val)
                expected = expected.next
                actual = actual.next
            else:
                self.fail('Unequal Lengths')

if __name__ == "__main__":
    unittest.main()
