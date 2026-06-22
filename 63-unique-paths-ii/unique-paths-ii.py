class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            if grid[i][0] == 1 :
                break
            else :
                dp[i][0] = 1
        for i in range(n):
            if grid[0][i] == 1 :
                break
            else :
                dp[0][i] = 1
        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j] == 1 :
                    dp[i][j] = 0
                else :
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
        