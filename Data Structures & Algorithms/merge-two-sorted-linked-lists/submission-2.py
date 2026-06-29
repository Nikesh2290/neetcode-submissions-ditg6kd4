# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        list2.next = self.mergeTwoLists(list1,list2.next)
        return list2
        # head = None
        # if l1.val <= l2.val:
        #     head = l1
        # else:
        #     head = l2
        # p1=p2=None
        # while l1 and l2:
        #     while l1 and l1.val <= l2.val:
        #         p1 = l1
        #         l1 = l1.next
        #     if l1 == None:
        #         p1.next = l2
        #         return head
        #     else:
        #         if p1:
        #             p1.next = l2
        #         while l2 and l1.val > l2.val:
        #             p2 = l2
        #             l2 = l2.next
        #         if l2 == None:
        #             p2.next = l1
        #             return head
        #         else:
        #             p2.next = l1
        # return head



                
            
            

                


        