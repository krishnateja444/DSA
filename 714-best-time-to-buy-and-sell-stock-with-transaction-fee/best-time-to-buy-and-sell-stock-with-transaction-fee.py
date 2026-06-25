class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        prev = [0]*2
        for i in range(n-1,-1,-1):
            curr = [0]*2
            curr[1] = max(-prices[i] + prev[0],prev[1])
            curr[0] = max(prices[i]+prev[1]-fee,prev[0])
            prev = curr
        return prev[1]