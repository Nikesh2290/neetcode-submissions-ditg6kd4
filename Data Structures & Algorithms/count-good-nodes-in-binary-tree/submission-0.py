# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self,root,gn_cnt,maxi):
        if not root:
            return 0
        if root.val >= maxi:
            gn_cnt[0] += 1
        self.solve(root.left,gn_cnt,max(maxi,root.val))
        self.solve(root.right,gn_cnt,max(maxi,root.val))
        return 
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return []
        gn_cnt = [0]
        maxi=float('-inf')
        self.solve(root,gn_cnt,maxi)
        return gn_cnt[0]
