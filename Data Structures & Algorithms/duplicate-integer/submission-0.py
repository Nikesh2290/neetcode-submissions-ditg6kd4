class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vis = {}
        for i,val in enumerate(nums):
            if val in vis:
                return True
            else:
                vis[val]=1
        return False