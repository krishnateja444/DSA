class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]
        dp = [[-1]*(len(cuts)) for _ in range(len(cuts))]
        def f(i,j):
            if i > j :
                return 0
            if dp[i][j] != -1 :
                return dp[i][j]
            mini = float('inf')
            for ind in range(i,j+1):
                cost = cuts[j+1] - cuts[i-1] + f(i,ind-1) + f(ind+1,j)
                mini = min(mini,cost)
            dp[i][j] = mini
            return dp[i][j]
        return f(1,len(cuts)-2)
        