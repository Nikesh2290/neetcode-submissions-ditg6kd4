class Solution:
    def solve(self,nums,i,n,prev,dp):
        if i >= n:
            return 0
        if dp[i][prev+1] != -1:
            return dp[i][prev+1]
        take = 0
        if prev == -1 or nums[i] > nums[prev]:
            take = 1 + self.solve(nums,i+1,n,i,dp)
        leave = self.solve(nums,i+1,n,prev,dp)
        dp[i][prev+1] = max(take,leave)
        return dp[i][prev+1]

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 1
        dp = [[-1 for _ in range(n+1)] for _ in range(n)]
        return self.solve(nums,0,n,-1,dp)