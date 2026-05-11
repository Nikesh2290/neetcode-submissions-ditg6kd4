class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            arr = [0]*9
            for j in range(9):
                if board[i][j] != '.':
                    arr[int(board[i][j])-1] += 1
                    if arr[int(board[i][j])-1]>1:
                        return False
        for i in range(9):
            arr = [0]*9
            for j in range(9):
                if board[j][i] != '.':
                    arr[int(board[j][i])-1] += 1
                    if arr[int(board[j][i])-1]>1:
                        return False
        for i in range(3):
            for j in range(3):
                row = 3*i
                col = 3*j
                arr = [0]*9
                for dr in range(3):
                    for dc in range(3):
                        if board[row+dr][col+dc] != '.':
                            arr[int(board[row+dr][col+dc])-1] += 1
                            if arr[int(board[row+dr][col+dc])-1]>1:
                                return False
        return True



                    
                    