class Solution:
    def solve(self,ans,temp,viscol,visindx,n,indx):
        if indx>=n:
            if len(temp) == n:
                ans.append(list(temp))
            return
        l = ["."]*n
        for i in range(n):
            if not viscol[i]:
                flag = False
                for val in visindx:
                    if abs(val[0]-indx) == abs(val[1]-i):
                        flag = True
                        break
                if flag:
                    continue
                viscol[i]=1
                visindx.append((indx,i))
                l[i] = 'Q'
                val = "".join(l)
                temp.append(val)
                self.solve(ans,temp,viscol,visindx,n,indx+1)
                viscol[i]=0
                visindx.pop()
                l[i] = '.'
                temp.pop()

                    

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        viscol = [0]*n
        temp = []
        visindx = []
        self.solve(ans,temp,viscol,visindx,n,0)
        return ans