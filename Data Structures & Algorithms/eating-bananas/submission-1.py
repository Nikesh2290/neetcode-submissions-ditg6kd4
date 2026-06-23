class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sortedpiles = sorted(piles)
        l = 1
        n = len(piles)
        r = sortedpiles[n-1]
        if n == h:
            return r
        k=r
        while l <= r:
            mid = (l+r)//2
            hour = 0
            bnana = mid
            for i in range(n):
                hour += math.ceil(sortedpiles[i]/bnana)
            if hour<=h:
                k = mid
                r = mid-1
            else:
                l = mid+1
        return k
            



