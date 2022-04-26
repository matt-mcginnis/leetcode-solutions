from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(l1.val + l2.val, None)
        curr_node = head
        next_node = None
        while l1.next and l2.next:
            next_node = ListNode(l1.next.val + l2.next.val)
            curr_node.next = next_node
            curr_node = next_node
            l1 = l1.next
            l2 = l2.next
        if l1.next:
            curr_node.next = l1.next
        elif l2.next:
            curr_node.next = l2.next
        else:
            return head
        return head
