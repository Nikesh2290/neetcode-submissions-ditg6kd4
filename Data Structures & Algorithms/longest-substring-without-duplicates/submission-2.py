class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        n = len(s)
        ans=0
        if n>0:
            ans=1
        prev_indx =0
        for i in range(len(s)):
            cnt = dic.get(s[i],0)
            if cnt == 0:
                dic[s[i]] = 1
            else:
                ans = max(ans,i-prev_indx)
                while s[i] != s[prev_indx]:
                    dic[s[prev_indx]] -= 1
                    prev_indx += 1
                prev_indx += 1
        ans = max(ans,n-prev_indx)
        return ans
            