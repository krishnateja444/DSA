class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1]*n for _ in range(m)]
        rsum = 0
        csum = 0
        for i in range(m):
            rsum += grid[i][0]
            dp[i][0] = rsum
        for i in range(n):
            csum += grid[0][i]
            dp[0][i] = csum
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j],dp[i][j-1])
        return dp[m-1][n-1]
        