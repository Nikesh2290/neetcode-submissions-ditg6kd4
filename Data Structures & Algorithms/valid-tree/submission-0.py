class Solution:
    def dfs(self,arr,vis,n,prev,i):
        vis[i] = 1
        check = True
        for nbr in arr[i]:
            if nbr != prev:
                if vis[nbr] == 1:
                    return False
                check = self.dfs(arr,vis,n,i,nbr)
                if not check:
                    return False
        return True
                
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        vis = [0]*n
        prev = -1
        ans = self.dfs(adj,vis,n,prev,0)
        if not ans:
            return False
        for i in range(n):
            if not vis[i]:
                return False
        return True