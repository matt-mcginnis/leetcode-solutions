from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1) Create dummy node to better handle single node edge cases
        2) Assign dummy node and curr_node variable to empty ListNode
        3) Add carry_over variable to store anything that needs to be carried to the next digit
        4) Iterate while there is something in l1, l2 or carry_over
        4) Keep value of sum l1.val and l2.val in carry_over and increment l1 and l2
        5) Add curr_node.next with value of 1's digit in carry_over variable (hence % 10)
        6) Increment curr_node
        7) Finally, store amount to be carried over by getting the 10's digit of carry_over (hence // 10)
        8) Return dummy.next when loop exits
        '''
        dummy = curr_node = ListNode(0)
        carry_over = 0
        while l1 or l2 or carry_over:
            if l1:
                carry_over += l1.val
                l1 = l1.next
            if l2:
                carry_over += l2.val
                l2 = l2.next
            if curr_node:
                curr_node.next = ListNode(carry_over % 10)
                curr_node = curr_node.next
                carry_over = carry_over // 10
        return dummy.next
