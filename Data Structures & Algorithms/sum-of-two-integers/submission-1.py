class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans=0
        carry=0
        for i in range(32):
            v1= a>>i&1
            v2= b>>i&1
            val = v1^v2^carry
            if v1+v2+carry>=2:
                carry=1
            else:
                carry=0
            if val:
                ans |= (1<<i)

        if ans>0x7FFFFFFF:
            ans = ~(ans^0xFFFFFFFF)
        return ans
