class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[n-1] > nums[0]:
            return nums[0]
        l=0
        r=n-1
        ans=1e9
        while l<r:
            mid = (l+r)//2
            ans = min(ans,nums[mid])
            if nums[mid]>=nums[0]:
                l = mid+1
            else:
                r = mid-1
        ans = min(ans,nums[l])
        return ans