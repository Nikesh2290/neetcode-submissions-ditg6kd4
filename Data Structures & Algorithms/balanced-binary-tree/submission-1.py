# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self,root):
        if root == None:
            return 0
        l = self.solve(root.left)
        r = self.solve(root.right)
        return 1+ max(l,r)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        if left == False or right == False:
            return False
        h1 = self.solve(root.left)
        h2 = self.solve(root.right)
        if abs(h1-h2) > 1:
            return False
        return True

        
        



        