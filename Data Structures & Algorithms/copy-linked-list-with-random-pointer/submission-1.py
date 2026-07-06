"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_head = None
        hd = head
        temp = None
        dic = {}
        while hd:
            node = Node(hd.val)
            dic[hd] = node
            if not copy_head:
                copy_head = node
                temp = copy_head
            else:
                temp.next = node
                temp = node
            hd = hd.next
        temp = copy_head
        hd = head
        while hd:
            nod = hd.random
            if nod != None:
                node = dic[nod]
                temp.random = node
            temp = temp.next
            hd = hd.next
        return copy_head


            

