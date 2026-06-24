class Solution:
    def minInsertions(self, s: str) -> int:
        s1 = s[::-1]
        m = len(s)
        prev = [0]*(m+1)
        for i in range(1,m+1):
            curr = [0]*(m+1)
            for j in range(1,m+1):
                if s[i-1] == s1[j-1]:
                    curr[j] = 1 + prev[j-1]
                else :
                    curr[j] = max(curr[j-1],prev[j])
            prev = curr
        return m - prev[m]
        