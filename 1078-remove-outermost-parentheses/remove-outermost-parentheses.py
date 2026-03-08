class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        s1 = ""
        i = 0
        j = 0
        c = 0
        while i < len(s):
            if s[i] == "(" :
                c += 1
                i += 1
            if s[i] == ")" :
                c -= 1
                i += 1
            if c == 0 :
                s1 += s[j+1 : i - 1]
                j = i
        return s1
                
            

        