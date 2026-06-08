class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = {}
        cnt1 = {}
        n1 = len(s1)
        n2 = len(s2)
        if n1>n2:
            return False
        for i in range(n1):
            cnt[s1[i]] = 1 + cnt.get(s1[i],0)
        i=j=0
        while j<n2:
            if cnt.get(s2[j],0) != 0:
                cnt1[s2[j]] = cnt1.get(s2[j],0)+1
            else:
                cnt1 = {}
                i=j+1
            if j-i+1 == n1:
                # print(cnt)
                # print(cnt1)
                if cnt == cnt1:
                    return True
                else:
                    cnt1[s2[i]] = cnt1.get(s2[i])-1
                    if cnt1[s2[i]] == 0:
                        del cnt1[s2[i]]
                    i+=1  
            j+=1
        return False


 

