class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        ans = []
        vis = {}
        for i in range(n):
            v = vis.get(strs[i]+str(i),-1)
            if v == -1:
                arr = []
                arr.append(strs[i])
                s1 = sorted(strs[i])
                vis[strs[i]+str(i)]=1
                for j in range(i+1,n):
                    if vis.get(strs[j]+str(j),-1) == -1:
                        s2 = sorted(strs[j])
                        if s1 == s2:
                            arr.append(strs[j])
                            vis[strs[j]+str(j)]=1
                ans.append(arr)
        return ans
            


