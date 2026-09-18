class Solution:
    def solve(self,coins,i,n,amount,dp):
        if amount == 0:
            return 0
        if amount < 0 or i >= n:
            return 1e5
        if dp[i][amount] != -1:
            return dp[i][amount]
        take = 1 + self.solve(coins,i,n,amount-coins[i],dp)
        leave = self.solve(coins,i+1,n,amount,dp)
        dp[i][amount] = min(take,leave)
        return dp[i][amount]
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        sorted_coins = sorted(coins,reverse=True)
        dp = [[-1 for _ in range(amount+1)] for _ in range(n)]
        ans = self.solve(sorted_coins,0,n,amount,dp)
        if ans >= 1e5:
            return -1
        return ans