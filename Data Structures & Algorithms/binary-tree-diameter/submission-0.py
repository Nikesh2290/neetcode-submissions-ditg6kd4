# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self,root):
        if root == None:
            return 0,0
        res1 = self.solve(root.left)
        res2 = self.solve(root.right)
        depth = max(res1[0],res2[0])
        # depth,max dia
        return 1+depth,max(res1[0]+res2[0],max(res1[1],res2[1]))
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None or (root.left == None and root.right == None):
            return 0
        ans = self.solve(root)
        return max(ans[0]-1,ans[1])
        