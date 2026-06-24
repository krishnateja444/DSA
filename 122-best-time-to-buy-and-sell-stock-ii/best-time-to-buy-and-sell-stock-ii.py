class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1]*2 for _ in range(n)]
        def f(ind,buy):
            if ind == n :
                return 0
            if dp[ind][buy] != -1 :
                return dp[ind][buy]
            if buy :
                take = f(ind+1,0) - prices[ind]  ## buy
                not_take = f(ind+1,1)             ## not buy
                profit = max(take,not_take)
            else :
                take = f(ind+1,1) + prices[ind]      ## sell
                not_take = f(ind+1,0)
                profit = max(take,not_take)
            dp[ind][buy] = profit
            return dp[ind][buy]
        return f(0,1)
        