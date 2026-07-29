# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        v = root
        while v:
            if (p.val >= v.val and q.val <= v.val) or (p.val <= v.val and q.val >= v.val):
                return  v
            elif p.val<v.val and q.val<v.val:
                v = v.left
            else:
                v = v.right
        return None