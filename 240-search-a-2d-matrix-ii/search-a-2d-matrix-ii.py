class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        max_row = -1
        max_col = -1
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            if mat[i][0] <= target <= mat[i][n-1] :
                max_row = i
        for j in range(n):
            if mat[0][j] <= target <= mat[m-1][j] :
                max_col = j
        if max_row == -1 :
            return False
        for i in range(max_row+1):
            left = 0
            right = max_col
            while left <= right :
                mid = (left + right)//2
                if mat[i][mid] == target :
                    return True
                if mat[i][mid] > target :
                    right = mid - 1
                else :
                    left = mid + 1
        return False
        