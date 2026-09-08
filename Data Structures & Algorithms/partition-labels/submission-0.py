class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        arr = [[-1, -1] for _ in range(26)]
        n = len(s)
        for i in range(n):
            indx = ord(s[i])-ord('a')
            if arr[indx][0] == -1:
                arr[indx][0] = i
            arr[indx][1] = i
        indx = 0
        ans = []
        while indx < n:
            si=indx
            ei = arr[ord(s[indx])-ord('a')][1]
            j=si
            while j<ei:
                if s[j] != s[si]:
                    ei = max(ei,arr[ord(s[j])-ord('a')][1])
                j += 1
            ans.append(ei-si+1)
            indx = ei+1
        return ans
        


