from collections import deque
class Solution:
    def findOrder(self, num: int, prereq: List[List[int]]) -> List[int]:
        degree = [0]*num
        arr = [[] for _ in range(num)]
        for a,b in prereq:
            degree[a] += 1
            arr[b].append(a)
        q = deque()
        for i in range(num):
            if degree[i] == 0:
                q.append(i)
        ans = []
        cnt = 0
        while q:
            val = q.popleft()
            ans.append(val)
            cnt += 1
            for nbr in arr[val]:
                degree[nbr] -= 1
                if degree[nbr] == 0:
                    q.append(nbr)
        if cnt < num:
            return []
        return ans
