from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr_node = ListNode(0)
        while l1 or l2:
            curr_val = 0
            if l1:
                curr_val += l1.val
                l1 = l1.next
            if l2:
                curr_val += l2.val
                l2 = l2.next
            curr_node.next = ListNode(curr_val)
            curr_node = curr_node.next
        return dummy.next
