class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for val in s:
            if val-1 not in s:
                cnt=1
                v = val
                while v+1 in s:
                    cnt += 1
                    v += 1
                ans = max(ans,cnt)
        return ans


            
            