class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        prev = [0]*n
        for i in range(m):
            curr = [0]*n
            for j in range(n):
                if i == 0 and j == 0 :
                    curr[j] = grid[i][j]
                elif j == 0 :
                    curr[j] = grid[i][j] + prev[j]
                elif i == 0 :
                    curr[j] = grid[i][j] + curr[j-1]    
                else:
                    curr[j] = grid[i][j] + min(prev[j],curr[j-1])
            prev = curr
        return prev[n-1]

        