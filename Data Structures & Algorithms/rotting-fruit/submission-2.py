from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m =  len(grid[0])
        q = deque()
        fresh_cnt = 0
        time=0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh_cnt += 1
        if fresh_cnt == 0:
            return time
        arr = [(1,0),(0,1),(-1,0),(0,-1)]
        while q:
            k = len(q)
            rot = False
            for _ in range(k):
                i,j = q.popleft()
                
                for dr,dc in arr:
                    r = i+dr
                    c = j+dc
                    if 0 <= r <n and 0 <= c <m:
                        if grid[r][c] == 1:
                            grid[r][c] = 2
                            q.append((r,c))
                            rot = True
                            fresh_cnt -= 1
            if rot:
                time += 1
        if fresh_cnt != 0:
            return -1
        return time