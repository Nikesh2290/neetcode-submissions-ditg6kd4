class Solution:
    def solve(self,n,ans,temp,lp,rp):
        if len(temp) == 2*n:
            ans.append(str(temp))
            return
        if lp <= rp:
            self.solve(n,ans,temp+'(',lp+1,rp)
        else:
            if lp<n:
                self.solve(n,ans,temp+'(',lp+1,rp)
            self.solve(n,ans,temp+')',lp,rp+1)
        return 

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        temp = ""
        self.solve(n,ans,temp,0,0)
        return ans