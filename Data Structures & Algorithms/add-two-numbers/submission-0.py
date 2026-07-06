# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = temp = None
        hl1 = l1
        hl2 = l2
        carry = 0
        while hl1 or hl2:
            v1 = v2 = 0
            if hl1:
                v1 = hl1.val
                hl1 = hl1.next
            if hl2:
                v2 = hl2.val
                hl2 = hl2.next
            val = v1+v2+carry
            node_val = val%10
            carry = val//10
            if not head:
                head = temp = ListNode(node_val)
            else:
                node = ListNode(node_val)
                temp.next = node
                temp = node
        if carry != 0:
            node = ListNode(carry)
            temp.next = node
            temp = node
        return head
