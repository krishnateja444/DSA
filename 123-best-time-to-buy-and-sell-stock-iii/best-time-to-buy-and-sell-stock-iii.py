class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1] * (2 + 1) for _ in range(2)] for _ in range(n + 1)]
        def f(ind,buy,cap):
            if dp[ind][buy][cap] != -1 :
                return dp[ind][buy][cap]
            if cap == 0 :
                dp[ind][buy][cap] = 0
                return 0
            if ind == len(prices) :
                dp[ind][buy][cap] = 0
                return 0
            if buy :
                dp[ind][buy][cap] = max(-prices[ind]+f(ind+1,0,cap),f(ind+1,1,cap))
            else :
                dp[ind][buy][cap] = max(prices[ind]+f(ind+1,1,cap-1),f(ind+1,0,cap))
            return dp[ind][buy][cap]
        return f(0,1,2)