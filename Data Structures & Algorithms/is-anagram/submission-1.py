class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s1 = sorted(s)
        # t1 = sorted(t)
        # if s1 == t1:
        #     return True
        # return False
        if len(s) != len(t):
            return False
        vis = [0]*26
        for i in range(len(s)):
            vis[ord(s[i])-ord('a')]+=1
            vis[ord(t[i])-ord('a')]-=1
        for i in range(26):
            if vis[i] != 0:
                return False
        return True
