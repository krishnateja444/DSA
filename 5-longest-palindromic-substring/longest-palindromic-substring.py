class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1] :
            return s
        def lcs(s1,s2):
            m = len(s1)
            n = len(s2)
            max_l = ""
            dp = [[""]*(n+1) for _ in range(m+1)]
            for i in range(1,m+1):
                for j in range(1,n+1):
                    if s1[i-1] == s2[j-1] :
                        dp[i][j] = dp[i-1][j-1] + s1[i-1]
                        if len(dp[i][j]) >= len(max_l) and dp[i][j] == dp[i][j][::-1]:
                            max_l = dp[i][j]
                    else :
                        dp[i][j] = ''
            return max_l
        return lcs(s,s[::-1])
        