class Solution:
    def findRow(self,matrix,target):
        n = len(matrix)
        si=0
        ei=n-1
        col = len(matrix[0])
        while si<=ei:
            mid = (si+ei)//2
            if matrix[mid][col-1] >= target and matrix[mid][0] <= target:
                return mid
            elif matrix[mid][0]> target:
                ei = mid-1
            else:
                si = mid+1
        return min(si,n-1)
            

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.findRow(matrix,target)
        m = len(matrix[0])
        si=0
        ei=m-1
        while si<=ei:
            mid = (si+ei)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                ei = mid-1
            else:
                si = mid+1
        return False
        