class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        jump = nums[0]
        if n<=1:
            return True
        indx = 0
        while indx<n-1 and jump>0:
            jump -= 1
            indx += 1
            jump = max(jump,nums[indx])
        if indx >= n-1:
            return True
        return False
        
