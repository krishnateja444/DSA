class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 :
            return 0
        n = len(coins)
        dp = [[float('inf')]*(amount+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 0
        for i in range(amount+1):
            if i % coins[0] == 0 :
                dp[0][i] = i // coins[0]
        for i in range(1,n):
            for j in range(1,amount+1):
                take = float('inf')
                if j >= coins[i] :
                    take = 1 + dp[i][j-coins[i]]
                not_take = dp[i-1][j]
                dp[i][j] = min(take,not_take)
        ans = dp[n-1][amount]
        if ans == float('inf') :
            return -1
        return ans
        