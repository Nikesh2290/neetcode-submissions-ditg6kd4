class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        j = n - 1
        i = 0
        while i < j:
            for col in range(n):
                matrix[i][col], matrix[j][col] = matrix[j][col], matrix[i][col]
            i += 1
            j -= 1
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return 