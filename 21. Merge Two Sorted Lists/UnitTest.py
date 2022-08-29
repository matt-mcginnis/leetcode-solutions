import unittest
from Solution import Solution, ListNode

class TestMergeTwoLists(unittest.TestCase):
    def test_1(self):
        l1 = ListNode(1, ListNode(2, ListNode(4, None)))
        l2 = ListNode(1, ListNode(3, ListNode(4, None)))
        sol = Solution()
        expected = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, None))))))
        actual = sol.mergeTwoLists(l1, l2)
        while actual or expected:
            if (actual and expected):
                self.assertEqual(expected.val, actual.val)
                expected = expected.next
                actual = actual.next
            else:
                self.fail('Not merged correctly.')
    def test_2(self):
        l1 = None
        l2 = None
        sol = Solution()
        expected = None
        actual = sol.mergeTwoLists(l1, l2)
        while actual or expected:
            if (actual and expected):
                self.assertEqual(expected.val, actual.val)
                expected = expected.next
                actual = actual.next
            else:
                self.fail('Not merged correctly.')
    def test_3(self):
        l1 = None
        l2 = ListNode(0, None)
        sol = Solution()
        expected = ListNode()
        actual = sol.mergeTwoLists(l1, l2)
        while actual or expected:
            if (actual and expected):
                self.assertEqual(expected.val, actual.val)
                expected = expected.next
                actual = actual.next
            else:
                self.fail('Not merged correctly.')

if __name__ == "__main__":
    unittest.main()