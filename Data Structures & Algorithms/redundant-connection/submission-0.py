class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        maxi=0
        for a1,a2 in edges:
            maxi = max(maxi,max(a1,a2))
        parent = list(range(maxi+1))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            p1 = find(x)
            p2 = find(y)
            if p1 == p2:
                return True
            parent[p1] = p2
            return False
        
        for a,b in edges:
            if union(a,b):
                return [a,b]
        return []