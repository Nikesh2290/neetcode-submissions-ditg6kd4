class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        ans=0
        for i in range(n):
            val = abs(nums[i])
            if nums[val-1] < 0:
                ans = val
                break
            nums[val-1] = -1*nums[val-1]
        for i in range(n):
            nums[i] = abs(nums[i])
        return ans