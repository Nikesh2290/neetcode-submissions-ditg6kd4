from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append((v,t))
        pq = [(0,k)] 
        visited = set()
        maxi=0
        while pq:
            time,node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            maxi = max(maxi,time)
            for nod,tim in adj[node]:
                if nod not in visited:
                    heapq.heappush(pq,(time+tim,nod))
        if len(visited) != n:
            return -1
        return maxi
