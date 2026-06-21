class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #dp = [[-1]*n for _ in range(m)]
        #for i in range(m):
        #   dp[i][0] = 1
        #for j in range(n):
        #   dp[0][j] = 1
        prev_row = [1]*n
        for i in range(1,m):
            curr = [1]*n
            for j in range(1,n):
                curr[j] = prev_row[j] + curr[j-1]
            prev_row = curr
        return prev_row[n-1]

        