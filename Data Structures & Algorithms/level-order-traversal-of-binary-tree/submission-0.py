# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        level = 0
        ans = []
        q.append([root,level])
        while q:
            node = q.popleft()
            if node[1] == level:
                x = [node[0].val]
                ans.append(x)
                level += 1
            else:
                ans[-1].append(node[0].val)
            if node[0].left:
                q.append([node[0].left,level])
            if node[0].right:
                q.append([node[0].right,level])
        return ans

