# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = 0
        temp=head
        while temp != None:
            temp = temp.next
            l += 1
        if l<=2:
            return
        mid = l//2
        temp1 = head
        i=1
        prev = head
        while i<=mid:
            prev = temp1
            temp1 = temp1.next
            i += 1
        nxt = temp1
        if l % 2 == 0:
            while nxt:
                nxt = temp1.next
                temp1.next = prev
                prev = temp1
                temp1 = nxt
        else:
            prev=temp1
            temp1 = temp1.next
            prev.next = None
            while nxt:
                nxt = temp1.next
                temp1.next = prev
                prev = temp1
                temp1 = nxt
        t1 = head
        t2 = prev
        while t1.next and t1.next != t2:
            nxt1 = t1.next
            nxt2 = t2.next
            t1.next = t2
            t2.next = nxt1
            t1 = nxt1
            t2 = nxt2
        if t1.next == None:
            return 
        t2.next = None
        return 
        





