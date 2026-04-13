class Solution:
    def reverse(self, x: int) -> int:
        ans=0
        sign=0
        if x<0:
            sign=-1
            x = abs(x)
        while x>0:
            ans = ans*10+(x%10)
            x = x//10
        if sign == -1:
            ans = -1*ans
        if ans<-1*(2**31) or ans>(2**31-1):
            return 0
        return ans