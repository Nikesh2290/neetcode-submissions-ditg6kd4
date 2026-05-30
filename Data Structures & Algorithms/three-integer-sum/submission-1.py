class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        n = len(nums)
        nums.sort()
        for i in range(1,n-1):
            val = nums[i]
            si=0
            ei=n-1
            while si<i and ei>i:
                if nums[i]+nums[si]+nums[ei] == 0:
                    answer.add(tuple([nums[si],nums[i],nums[ei]]))
                    si+=1
                elif nums[i]+nums[si]+nums[ei] >0:
                    ei-=1
                else:
                    si+=1
        return list(answer)
