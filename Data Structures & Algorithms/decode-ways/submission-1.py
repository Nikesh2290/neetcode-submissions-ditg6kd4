class Solution:
    def solve(self, s: str, indx: int, n: int, dp: list[int]):
        if indx >= n-1:
            return 1
        if dp[indx] != -1:
            return dp[indx]
        if s[indx] == "0" or s[indx+1] == "0" or int(s[indx:indx+2])>26 or (indx+2<n and s[indx+2] == "0"):
            dp[indx] = self.solve(s,indx+1,n,dp)
        else:
            dp[indx] =  self.solve(s,indx+1,n,dp)+self.solve(s,indx+2,n,dp)
        return dp[indx]

            
        
        dp[indx] = self.solve(s,indx+2,n,dp)
        
        
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == "0":
            return 0
        for i in range(1,n):
            if s[i] == "0" and (int(s[i-1])>2 or s[i-1] == "0"):
                return 0
        if n<=1:
            return n
        dp = [-1]*n
        return self.solve(s,0,n,dp)