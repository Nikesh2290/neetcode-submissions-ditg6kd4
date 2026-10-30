class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = len(matrix)
        c = len(matrix[0])
        sr,er = 0,r-1
        sc,ec = 0,c-1
        ans = []
        while sr<=er and sc<=ec:
            for col in range(sc,ec+1):
                ans.append(matrix[sr][col])
                
            for row in range(sr+1,er+1):
                ans.append(matrix[row][ec])
            if sr < er:
                for col in range(ec-1,sc-1,-1):
                    ans.append(matrix[er][col])
            if sc<ec:
                for row in range(er-1,sr,-1):
                    ans.append(matrix[row][sc])
            sr += 1
            er -= 1
            sc += 1
            ec -= 1
        return ans
