class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        prev_row = [0]*n
        for i in range(m):
            curr = [0]*n
            for j in range(n):
                if grid[i][j] == 1 :
                    curr[j] = 0
                elif i == 0 and j == 0:
                    curr[j] = 1
                else :
                    if i > 0 :
                        prev_r = prev_row[j]
                    else :
                        prev_r = 0
                    if j > 0 :
                        curr_ = curr[j-1]
                    else :
                        curr_ = 0
                    curr[j] = curr_ + prev_r
            prev_row = curr
        return prev_row[n-1]