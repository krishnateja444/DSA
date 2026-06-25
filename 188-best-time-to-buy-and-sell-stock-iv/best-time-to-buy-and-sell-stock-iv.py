class Solution:
    def maxProfit(self, cap: int, prices: List[int]) -> int:
        n = len(prices)
        trans = 2*cap 
        dp = [[0]*(trans+1) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(trans):
                if j % 2 == 0 :
                    dp[i][j] = max(-prices[i]+dp[i+1][j+1],dp[i+1][j])
                else :
                    dp[i][j] = max(prices[i]+dp[i+1][j+1],dp[i+1][j])
        return dp[0][0]

        