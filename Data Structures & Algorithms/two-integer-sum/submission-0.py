class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        n = len(nums)
        dic[nums[0]] = 0
        for i in range(1,n):
            val = nums[i]
            indx = dic.get(target-nums[i],-1)
            if indx != -1:
                return [indx,i]
            dic[nums[i]] = i
        return [-1,-1]
