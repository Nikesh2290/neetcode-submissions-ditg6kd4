from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        q = deque()
        for i in range(n):
            if board[i][0] == 'O':
                vis[i][0] = 1
                q.append((i,0))
            if board[i][m-1] == 'O':
                vis[i][m-1] = 1
                q.append((i,m-1))
        for j in range(1,m-1):
            if board[0][j] == 'O':
                vis[0][j] = 1
                q.append((0,j))
            if board[n-1][j] == 'O':
                vis[n-1][j] = 1
                q.append((n-1,j))
        nbr = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c = q.popleft()
            for dr,dc in nbr:
                i,j = r+dr,c+dc
                if 0<=i<n and 0<=j<m:
                    if not vis[i][j] and board[i][j] == 'O':
                        vis[i][j] = 1
                        q.append((i,j))
        for i in range(1,n-1):
            for j in range(1,m-1):
                if board[i][j] == 'O' and not vis[i][j]:
                    board[i][j] = 'X'
        return 
                        
