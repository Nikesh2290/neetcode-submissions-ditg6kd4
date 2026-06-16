class Solution:
    def minWindow(self, s: str, t: str) -> str:
        arr = [0]*52
        n = len(s)
        m = len(t)
        if m>n or m == 0:
            return ""
        # for i in range(n):
        #     if 'A'<=s[i]<='Z':
        #         arr[ord(s[i])-ord('A')] += 1
        #     else:
        #         arr[ord(s[i])-ord('a')+26] += 1
        # for i in range(m):
        #     if 'A'<=t[i]<='Z':
        #         arr[ord(t[i])-ord('A')] -= 1
        #         if arr[ord(t[i])-ord('A')] < 0:
        #             return ""
        #     else:
        #         arr[ord(t[i])-ord('a')+26] -= 1
        #         if arr[ord(t[i])-ord('a')+26] <0:
        #             return ""
        dict1 = {}
        distinct_char=0
        for i in range(m):
            dict1[t[i]] = 1 + dict1.get(t[i],0)
            if dict1[t[i]] == 1:
                distinct_char += 1
        pi=0
        dict2={}
        ans = ""
        distinct_char1=0
        for i in range(n):
            if dict1.get(s[i],0) != 0:
                dict2[s[i]] = 1 + dict2.get(s[i],0)
                if dict2[s[i]] == dict1[s[i]]:
                    distinct_char1 += 1
                    if distinct_char1 == distinct_char:
                        while pi<=i:
                            if ans == "" or i-pi+1<len(ans):
                                ans = s[pi:i+1]
                            if dict1.get(s[pi],0) != 0:
                                if dict2[s[pi]] > dict1[s[pi]]:
                                    dict2[s[pi]] -= 1
                                    pi += 1
                                else:
                                    dict2[s[pi]] -= 1
                                    distinct_char1 -= 1
                                    pi += 1
                                    break
                            else:
                                pi += 1
        return ans
                
                                
                                    



                
                



        
        