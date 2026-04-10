class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [-1]*(n+1)
        for i in range(n+1):
            num=i
            val=0
            while num>0:
                if ans[num] != -1:
                    val += ans[num]
                    break
                val += 1
                num = num&(num-1)
            ans[i]=val
        return ans


