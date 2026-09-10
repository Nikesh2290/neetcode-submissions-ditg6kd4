class Solution:
    def solve(self,n,dp):
        if n<=2:
            if dp[n] == -1:
                dp[n] = n
            return n
        if dp[n] != -1:
            return dp[n]
        dp[n] = self.solve(n-1,dp) + self.solve(n-2,dp)
        return dp[n]
        
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [-1]*(n+1)
        dp[0] = 0
        return self.solve(n,dp)