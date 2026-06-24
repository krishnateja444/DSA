class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        #dp = [[-1]*2 for _ in range(n+1)]
        prev = [0]*2
        for i in range(n-1,-1,-1):
            curr = [-1]*2
            curr[1] = max(prev[0] - prices[i],prev[1])
            curr[0] = max(prev[1] + prices[i],prev[0])
            prev = curr
        return prev[1]