class Solution:
    def solve(self,digits,mapp,ans,temp,indx,n):
        if indx>=n:
            ans.append(str(temp))
            return
        digit = int(digits[indx])
        s = mapp[digit]
        for char in s:
            self.solve(digits,mapp,ans,temp+char,indx+1,n)
        return

    def letterCombinations(self, digits: str) -> List[str]:
        mapp = {2: "abc",
                3: "def",
                4: "ghi",
                5: "jkl",
                6: "mno",
                7: "pqrs",
                8: "tuv",
                9: "wxyz"
                }
        ans = []
        temp = ""
        n = len(digits)
        if n<=0:
            return ans
        self.solve(digits,mapp,ans,temp,0,n)
        return ans