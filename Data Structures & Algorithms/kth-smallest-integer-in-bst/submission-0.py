# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self,root,k,cnt):
        if root is None:
            return False,cnt
        l = self.solve(root.left,k,cnt)
        if l[0]:
            return l
        if l[1]+1 == k:
            return True,root.val
        r = self.solve(root.right,k,l[1]+1)
        return r
        

        
        

        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = self.solve(root,k,0)
        return ans[1]

        