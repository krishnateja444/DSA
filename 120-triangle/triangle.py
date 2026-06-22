class Solution:
    def minimumTotal(self, t: List[List[int]]) -> int:
        m = len(t)
        dp = [[-1]*(i+1) for i in range(m)]
        dp[0][0] = t[0][0]
        for i in range(1,m):
            for j in range(i+1):
                if j == 0 :
                    dp[i][j] = t[i][j] + dp[i-1][0]
                elif j == i :
                    dp[i][j] = t[i][j] + dp[i-1][j-1]
                else :
                    up = dp[i-1][j]
                    left = dp[i-1][j-1]
                    dp[i][j] = t[i][j] + min(up,left)
        return min(dp[m-1])
        