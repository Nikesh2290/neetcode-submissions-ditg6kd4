class Solution:
    def solve(self,nums,target,indx,n,final,temp):
        if target == 0:
            final.append(list(temp))
            return 
        if indx>=n or target<0:
            return 
        temp.append(nums[indx])
        self.solve(nums,target-nums[indx],indx,n,final,temp)
        temp.pop()
        self.solve(nums,target,indx+1,n,final,temp)
        return
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        final = []
        temp = []
        self.solve(nums,target,0,n,final,temp)
        return final