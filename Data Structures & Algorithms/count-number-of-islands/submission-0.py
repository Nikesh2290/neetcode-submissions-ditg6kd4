class Solution:
    def solve(self,grid,vis,i,j,m,n):
        if i<0 or i>=n or j<0 or j>=m:
            return
        arr = [(0,1),(1,0),(-1,0),(0,-1)]
        for val in arr:
            r = i+val[0]
            c = j+val[1]
            if r>=0 and r<n and c>=0 and c<m and grid[r][c] == "1" and not vis[r][c]:
                vis[r][c] = 1
                self.solve(grid,vis,r,c,m,n)
        return

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1" and not vis[i][j]:
                    ans += 1
                    vis[i][j] = 1
                    self.solve(grid,vis,i,j,m,n)
        return ans