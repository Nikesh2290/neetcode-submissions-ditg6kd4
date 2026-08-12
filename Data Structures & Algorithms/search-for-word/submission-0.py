class Solution:
    def solve(self,board,word,i,j,n,m,l,indx,vis):
        if indx == l:
            return True
        if j>0 and vis[i][j-1] == 0 and board[i][j-1] == word[indx]:
            vis[i][j-1] = 1
            left = self.solve(board,word,i,j-1,n,m,l,indx+1,vis)
            vis[i][j-1] = 0
            if left:
                return True
        if j<m-1 and vis[i][j+1] == 0 and board[i][j+1] == word[indx]:
            vis[i][j+1] = 1
            right = self.solve(board,word,i,j+1,n,m,l,indx+1,vis)
            vis[i][j+1] = 0
            if right:
                return True
        if i>0 and vis[i-1][j] == 0 and board[i-1][j] == word[indx]:
            vis[i-1][j] = 1
            top = self.solve(board,word,i-1,j,n,m,l,indx+1,vis)
            vis[i-1][j] = 0
            if top:
                return True
        if i<n-1 and vis[i+1][j] == 0 and board[i+1][j] == word[indx]:
            vis[i+1][j] = 1
            bottom = self.solve(board,word,i+1,j,n,m,l,indx+1,vis)
            vis[i+1][j] = 0
            if bottom:
                return True
        return False
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        l = len(word)
        ans = False
        vis = [[0 for _ in range(m)] for _ in range(n)]
        print(vis)
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    vis[i][j] = 1
                    ans = self.solve(board,word,i,j,n,m,l,1,vis)
                    if ans:
                        return ans
                    vis[i][j]=0
        return ans