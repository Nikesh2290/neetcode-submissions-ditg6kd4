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
        dp = [[0, 0] for _ in range(n+1)]
        # return self.solve(nums,dp,0,n-1)
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1])
            dp[i][1] = nums[i] + dp[i-1][0]
        return max(dp[n-1][0],dp[n-1][1])
        