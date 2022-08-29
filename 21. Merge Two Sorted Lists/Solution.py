from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                curr_node.next = list1
                curr_node = curr_node.next
                list1 = list1.next
            else:
                curr_node.next = list2
                curr_node = curr_node.next
                list2 = list2.next

        if list1 or list2:
            curr_node.next = list1 if list1 else list2
        
        return dummy.next

sol = Solution()

# l1 = ListNode(1, ListNode(2, ListNode(4, None)))
# l2 = ListNode(1, ListNode(3, ListNode(4, None)))

l1 = None
l2 = ListNode(0, None)

mrg_list = sol.mergeTwoLists(l1, l2)
while mrg_list:
    print(mrg_list.val)
    mrg_list = mrg_list.next