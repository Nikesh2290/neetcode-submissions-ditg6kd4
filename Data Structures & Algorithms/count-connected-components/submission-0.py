class Solution:
    def dfs(self,n,adj,vis,i):
        vis[i] = 1
        for nbr in adj[i]:
            if not vis[nbr]:
                self.dfs(n,adj,vis,nbr)
        return
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        vis = [0]*(n)
        ans=0
        for i in range(n):
            if not vis[i]:
                self.dfs(n,adj,vis,i)
                ans += 1
        return ans
