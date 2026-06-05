class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre_max = [0]*n
        nxt_max = [0]*n
        pre_max[0] = height[0]
        nxt_max[n-1] = height[n-1]
        for i in range(1,n):
            pre_max[i] = max(pre_max[i-1],height[i])
        for i in  range(n-2,-1,-1):
            nxt_max[i] = max(nxt_max[i+1],height[i])
        ans=0
        for i in range(1,n-1):
            x = min(pre_max[i-1],nxt_max[i+1])
            if x>height[i]:
                ans += (x-height[i])
        return ans