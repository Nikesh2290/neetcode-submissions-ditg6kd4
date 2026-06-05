class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy=sell=prices[0]
        profit = 0
        for i in range(1,n):
            if prices[i]<buy:
                buy = sell = prices[i]
            else:
                sell = max(sell,prices[i])
            profit = max(profit,sell-buy)
        return profit                
