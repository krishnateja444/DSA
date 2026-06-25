class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        c = 2
        n = len(prices)
        dp = [[0] * (c + 1) for _ in range(2)] 
        for ind in range(n-1,-1,-1):
            curr = [[0] * (c + 1) for _ in range(2)] 
            for cap in range(1,c+1):
                curr[1][cap] = max(-prices[ind]+dp[0][cap],dp[1][cap])
                curr[0][cap] = max(prices[ind]+dp[1][cap-1],dp[0][cap])
            dp = curr
        return dp[1][c]