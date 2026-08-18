class Solution:
    def solve(self,grid,vis,i,j,m,n):
        arr = [(1,0),(0,1),(-1,0),(0,-1)]
        area = 1
        for dr,dc in arr:
            r = i+dr
            c = j+dc
            if 0 <= r < n and 0 <= c < m:
                if grid[r][c] and not vis[r][c]:
                    vis[r][c] = 1
                    val = self.solve(grid,vis,r,c,m,n)
                    area += val
        return area
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] and not vis[i][j]:
                    vis[i][j] = 1
                    area = self.solve(grid,vis,i,j,m,n)
                    ans = max(ans,area)
        return ans