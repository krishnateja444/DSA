class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[-1]*2 for _ in range(n)] for _ in range(m)]
        def solve(i,j,p):
            if i == m or j == n :
                return 0
            if dp[i][j][p] != - 1 :
                return dp[i][j][p]
            if i == m - 1 and j == n - 1 :
                dp[i][j][p] = 1
                return 1
            if grid[i][j] == 0 :
                dp[i][j][p] = solve(i+1,j,0) + solve(i,j+1,1)
                return dp[i][j][p]
            if grid[i][j] == 1 :
                if p == 0 :
                    dp[i][j][p] = solve(i,j+1,1)
                    return dp[i][j][p]
                if p == 1:
                    dp[i][j][p] = solve(i+1,j,0)
                    return dp[i][j][p]
        return solve(0,0,-1) % (1000000007)
            
            
            



        