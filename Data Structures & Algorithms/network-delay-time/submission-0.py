from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        for u,v,t in times:
            adj[u].append((v,t))
        vis = [False]*(n+1)
        timearr = [0]*(n+1)
        cnt = 0
        q = deque()
        q.append((k,0))
        vis[k] = True
        cnt += 1
        while q:
            node,time = q.popleft()
            for v,t in adj[node]:
                if not vis[v]:
                    vis[v] = True
                    q.append((v,t+time))
                    timearr[v] = t+time
                    cnt += 1
                elif t+time<timearr[v]:
                    timearr[v] = t+time
                    q.append((v,t+time))
        if cnt<n:
            return -1
        maxi = 0
        for i in range(len(timearr)):
            maxi = max(maxi,timearr[i])
        return maxi
                
        