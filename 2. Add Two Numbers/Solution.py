from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr_node = ListNode(0)
        carry_over = 0
        while l1 or l2 or carry_over:
            if l1:
                carry_over += l1.val
                l1 = l1.next
            if l2:
                carry_over += l2.val
                l2 = l2.next
            curr_node.next = ListNode(carry_over % 10)
            curr_node = curr_node.next
            carry_over = carry_over // 10
        return dummy.next
