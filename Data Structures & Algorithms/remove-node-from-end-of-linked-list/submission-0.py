# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        temp = head
        while temp != None:
            l+= 1
            temp = temp.next
        if n == l:
            head = head.next
            return head
        indx = l-n-1
        temp = head
        while indx > 0:
            indx -= 1
            temp = temp.next
            
        temp.next = temp.next.next
        return head
        
