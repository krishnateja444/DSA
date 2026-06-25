class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        prev1 = [0]*2
        prev2 = [0]*2
        for i in range(n-1,-1,-1):
            curr = [0]*2
            curr[1] = max(-prices[i] + prev1[0],prev1[1])
            curr[0] = max(prices[i]+prev2[1],prev1[0])
            prev2 = prev1
            prev1 = curr
        return prev1[1]