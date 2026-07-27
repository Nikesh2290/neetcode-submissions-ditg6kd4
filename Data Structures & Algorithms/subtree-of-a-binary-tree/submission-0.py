# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def solve(self,root1,root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None or root1.val != root2.val:
            return False
        left = self.solve(root1.left,root2.left)
        if not left:
            return False
        right = self.solve(root1.right,root2.right)
        if not right:
            return False
        return True
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        if root.val == subRoot.val:
            check = self.solve(root,subRoot)
            if check:
                return True
        left = self.isSubtree(root.left,subRoot)
        if left:
            return True
        right = self.isSubtree(root.right,subRoot)
        if right:
            return True
        return False
            