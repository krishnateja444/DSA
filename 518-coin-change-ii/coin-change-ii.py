class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0 :
            return 1
        n = len(coins)
        prev = [0]*(amount+1)
        for i in range(amount+1):
            if i % coins[0] == 0 :
                prev[i] = 1
        for i in range(1,n):
            curr = [0]*(amount+1)
            curr[0] = 1
            for j in range(1,amount+1):
                take = 0
                if coins[i] <= j :
                    take = curr[j-coins[i]]
                not_take = prev[j]
                curr[j] = take + not_take
            prev = curr
        return prev[amount]

        