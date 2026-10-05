class Solution:
    def solve(self,nums,i,n,total,dp):
        if total == 0:
            return True
        if total<0 or i>=n:
            return False
        if dp[i][total] != -1:
            return dp[i][total]
        take = self.solve(nums,i+1,n,total-nums[i],dp)
        leave  = self.solve(nums,i+1,n,total,dp)
        dp[i][total] = take|leave
        return dp[i][total]

    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return False
        total=0
        for i in range(n):
            total += nums[i]
        if total%2 != 0:
            return False
        dp = [[-1 for _ in range(total+1)] for _ in range(n)]
        ans = self.solve(nums,0,n,(total//2),dp)
        return ans