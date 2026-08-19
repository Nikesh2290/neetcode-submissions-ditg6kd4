from collections import deque
class Solution:
    
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i,j,0))
        nbr = [(1,0),(0,1),(-1,0),(0,-1)]
        while q:
            k = len(q)
            for _ in range(k):
                r,c,d = q.popleft()
                for dr,dc in nbr:
                    i = r+dr
                    j = c+dc
                    if 0<= i <n and 0 <= j <m:
                        if grid[i][j] == 2147483647:
                            grid[i][j] = d+1
                            q.append((i,j,d+1))
        return
        
