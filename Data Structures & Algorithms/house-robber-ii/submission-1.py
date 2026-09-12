class Solution:
    # def solve(self,nums,n,indx,dp,taken):
    #     if indx >= n:
    #         return 0
    #     if dp[indx][taken] != -1:
    #         return dp[indx][taken]
    #     take = -1
    #     if not taken:
    #         take = nums[indx] + self.solve(nums,n,indx+1,dp,1)
    #     leave = self.solve(nums,n,indx+1,dp,0)
    #     dp[indx][taken] = max(take,leave)
    #     return dp[indx][taken]

    def solve(self,nums,n,indx,dp):
        if indx >= n:
            return 0
        if dp[indx] != -1:
            return dp[indx]
        take = nums[indx] + self.solve(nums,n,indx+2,dp)
        leave = self.solve(nums,n,indx+1,dp)
        dp[indx] = max(take,leave)
        return dp[indx]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # dp1 = [[-1,-1] for _ in range(n)]
        # dp2 = [[-1,-1] for _ in range(n)]
        # ans = max(self.solve(nums,n-1,0,dp1,0),self.solve(nums,n,1,dp2,0))
        dp1 = [-1]*n
        dp2 = [-1]*n
        ans = max(self.solve(nums,n-1,0,dp1),self.solve(nums,n,1,dp2))
        return ans