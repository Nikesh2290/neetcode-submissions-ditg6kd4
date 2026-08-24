from collections import deque
class Solution:
    # def dfs(self,n,adj,vis,i):
    #     vis[i] = 1
    #     for nbr in adj[i]:
    #         if not vis[nbr]:
    #             self.dfs(n,adj,vis,nbr)
    #     return
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        vis = [0]*(n)
        ans=0
        # method1: dfs
        # for i in range(n):
        #     if not vis[i]:
        #         self.dfs(n,adj,vis,i)
        #         ans += 1
        # return ans

        # method2:bfs
        q = deque()
        for i in range(n):
            if not vis[i]:
                q.append(i)
                vis[i] = 1
                ans += 1
                while q:
                    val = q.popleft()
                    for nbr in adj[val]:
                        if not vis[nbr]:
                            vis[nbr] = 1
                            q.append(nbr)
        return ans


