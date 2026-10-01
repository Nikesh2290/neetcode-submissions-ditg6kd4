class Solution:
    def solve(self,s,i,j,n,word_set,dp):
        if j >= n:
            if s[i:] in word_set:
                return True
            return False
        if dp[i][j] != -1:
             return dp[i][j]
        take = False
        if s[i:j+1] in word_set:
            take = self.solve(s,j+1,j+1,n,word_set,dp)
        leave = self.solve(s,i,j+1,n,word_set,dp)
        dp[i][j] = take|leave
        return dp[i][j]
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        
        return self.solve(s,0,0,n,word_set,dp)