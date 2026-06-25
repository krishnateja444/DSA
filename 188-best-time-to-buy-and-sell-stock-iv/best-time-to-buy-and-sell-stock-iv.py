class Solution:
    def maxProfit(self, cap: int, prices: List[int]) -> int:
        n = len(prices)
        trans = 2*cap 
        dp = [0]*(trans+1)
        for i in range(n-1,-1,-1):
            curr = [0]*(trans+1)
            for j in range(trans):
                if j % 2 == 0 :
                    curr[j] = max(-prices[i]+dp[j+1],dp[j])
                else :
                    curr[j] = max(prices[i]+dp[j+1],dp[j])
            dp = curr
        return dp[0]

        