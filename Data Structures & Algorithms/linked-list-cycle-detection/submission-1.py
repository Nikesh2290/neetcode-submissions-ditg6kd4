# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        n1 = n2 = head
        while n2 and n2.next and n2.next.next:
            n1 = n1.next
            n2 = n2.next.next
            if n1 == n2:
                return True
        return False