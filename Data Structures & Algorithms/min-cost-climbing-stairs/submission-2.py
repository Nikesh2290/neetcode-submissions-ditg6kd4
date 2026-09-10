class Solution:
    # def solve(self,cost,n,dp):
    #     if n <= 1:
    #         return 0

    #     if dp[n] != -1:
    #         return dp[n]

    #     dp[n] =  min(cost[n-1]+self.solve(cost,n-1,dp), cost[n-2]+self.solve(cost,n-2,dp))
    #     return dp[n]


    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 2:
            return min(cost[0],cost[1])
        # dp = [-1]*(n+1)
        # return self.solve(cost,n,dp)
        prev1 = 0
        prev2 = 0
        for i in range(2,n+1):
            curr = min(cost[i-1] + prev1,cost[i-2]+prev2)
            prev2 = prev1
            prev1 = curr
        return prev1