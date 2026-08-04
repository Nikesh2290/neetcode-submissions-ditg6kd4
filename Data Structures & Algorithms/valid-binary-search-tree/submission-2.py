# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self,l,r,root):
        if root is None:
            return True
        if l and l.val >= root.val:
            return False
        if r and r.val<= root.val:
            return False
        return self.solve(l,root,root.left) and self.solve(root,r,root.right)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.solve(None,None,root)
        
            