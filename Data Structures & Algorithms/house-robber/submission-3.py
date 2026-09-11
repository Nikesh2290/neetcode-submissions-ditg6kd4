class Solution:
    # def solve(self,nums,dp,taken,indx):
    #     if indx < 0:
    #         return 0
        
    #     if dp[indx][taken] != -1:
    #         return dp[indx][taken]
    #     take = -1
    #     if not taken:
    #         take = nums[indx] + self.solve(nums,dp,1,indx-1)
    #     leave = self.solve(nums,dp,0,indx-1)
    #     # print(indx,take,leave)
    #     dp[indx][taken] = max(take,leave)
    #     return dp[indx][taken]
        
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # dp = [[0, 0] for _ in range(n+1)]
        # return self.solve(nums,dp,0,n-1)
        leave = 0
        take = nums[0]
        for i in range(1,n):
            leave1 = max(leave,take)
            take1 = nums[i] + leave
            leave = leave1
            take = take1
        return max(leave,take)
        