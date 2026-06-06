class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=j=0
        n = len(s)
        cnt = {}
        maxf=0
        res=0
        while i<n and j<n:
            cnt[s[j]] = 1+cnt.get(s[j],0)
            maxf = max(maxf,cnt[s[j]])
            if (j-i+1)-maxf<=k:
                res = max(res,j-i+1)
            else:
                if maxf == cnt.get(s[i],0):
                    maxf -= 1
                cnt[s[i]] = cnt.get(s[i])-1
                i+=1
            j+=1
        return res

