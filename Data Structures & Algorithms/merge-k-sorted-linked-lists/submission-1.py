# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def solve(self,head,head1):
        if head1 == None:
            return head
        ans = None
        h = None
        while head and head1:
            if h == None:
                if head.val <= head1.val:
                    ans = h = head
                    head = head.next
                else:
                    ans = h = head1
                    head1 = head1.next
            else:
                if head.val <= head1.val:
                    h.next = head
                    head = head.next
                    h = h.next
                else:
                    h.next = head1
                    head1 = head1.next
                    h = h.next
        while head:
            h.next = head
            head = head.next
            h = h.next
        while head1:
            h.next = head1
            head1 = head1.next
            h = h.next
        return ans

            
            


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        if n==1:
            return lists[0]
            
        head = lists[0]
        for i in range(1,n):
            head1 = lists[i]
            head = self.solve(head,head1)

        return head 
