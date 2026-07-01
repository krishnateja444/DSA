class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l_c = 0
        r = 0
        for i in range(len(s)):
            if s[i] == '(' :
                l_c += 1
            elif l_c > 0 and s[i] == ')' :
                l_c -= 1
            else :
                r += 1

        return abs(l_c + r)
        