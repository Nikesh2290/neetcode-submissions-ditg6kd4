class Solution:
    def solve(self, s: str, indx: int, n: int, dp: list[int]):
        if indx >= n:
            return 1
        if s[indx] == "0":
            return 0
        if dp[indx] != -1:
            return dp[indx]
        
        dp[indx] = self.solve(s,indx+1,n,dp)
        if indx+1<n and  (int(s[indx:indx+2]) >= 10 and int(s[indx:indx+2])<=26):
            dp[indx] += self.solve(s,indx+2,n,dp)
        return dp[indx] 
        
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1]*n
        return self.solve(s,0,n,dp)