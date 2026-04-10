class Solution:
    def reverseBits(self, n: int) -> int:
        bin = ""
        val=31
        ans=0
        m=1
        while val>=0:
            if (n&(1<<val)):
                ans += m
            m *= 2
            val-=1
            print("ans",ans)
            print(m)
            print(n)
        return ans
            
        

        
            
