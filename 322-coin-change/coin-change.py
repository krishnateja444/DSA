class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 :
            return 0
        n = len(coins)
        #dp = [[float('inf')]*(amount+1) for _ in range(n)]
        prev = [float('inf')]*(amount+1)
        #for i in range(n):
            #dp[i][0] = 0
        prev[0] = 0
        for i in range(amount+1):
            if i % coins[0] == 0 :
                prev[i] = i // coins[0]
        for i in range(1,n):
            curr = [float('inf')]*(amount+1)
            prev[0] = curr[0] = 0
            for j in range(1,amount+1):
                take = float('inf')
                if j >= coins[i] :
                    take = 1 + curr[j-coins[i]]
                not_take = prev[j]
                curr[j] = min(take,not_take)
            prev = curr
        ans = prev[amount]
        if ans == float('inf') :
            return -1
        return ans
        