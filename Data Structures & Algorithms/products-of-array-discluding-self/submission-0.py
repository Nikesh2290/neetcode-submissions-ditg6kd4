class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        n = len(nums)
        cnt_0 = 0
        output = [0]*n
        for i in range(n):
            if nums[i] != 0:
                prod *= nums[i]
            else:
                cnt_0 +=1
        if cnt_0>1:
            return output
        for i in range(n):
            if cnt_0 == 1:
                if nums[i] == 0:
                    output[i] = prod
            else:
                output[i] = prod//nums[i]
        return output