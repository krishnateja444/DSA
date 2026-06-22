class Solution:
    def minimumTotal(self, t: List[List[int]]) -> int:
        m = len(t)
        #dp = [[-1]*(i+1) for i in range(m)]
        #dp[0][0] = t[0][0]
        prev = []
        prev.append(t[0][0])
        for i in range(1,m):
            temp = [0]*(i+1)
            for j in range(i+1):
                if j == 0 :
                    temp[j] = t[i][j] + prev[j]
                elif j == i :
                    temp[j] = t[i][j] + prev[j-1]
                else :
                    up = prev[j]
                    left = prev[j-1]
                    temp[j] = t[i][j] + min(up,left)
            prev = temp
        return min(prev)
        