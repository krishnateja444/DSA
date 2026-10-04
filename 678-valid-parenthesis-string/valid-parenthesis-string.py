class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}
        def solve(i,l_c):
            if i == len(s):
                if l_c == 0 :
                    return True
                return False
            if (i,l_c) in dp :
                return dp[(i,l_c)]
            if l_c < 0 :
                dp[(i,l_c)] = False
                return False
            if s[i] == '(':
                dp[(i,l_c)] = solve(i+1,l_c+1)
                return dp[(i,l_c)]
            elif s[i] == ')' :
                dp[(i,l_c)] = solve(i+1,l_c-1)
                return dp[(i,l_c)]
            else :
                dp[(i,l_c)] = solve(i+1,l_c) or solve(i+1,l_c-1) or solve(i+1,l_c + 1)
                return dp[(i,l_c)]
        
        return solve(0,0)


        """left_min = 0
        left_max = 0
        if s[0] == ')' :
            return False
        for i in range(len(s)):
            if s[i] == '(' :
                left_min += 1
                left_max += 1
            elif s[i] == ')' :
                left_min -= 1
                if left_min < 0 :
                    left_min = 0
                left_max -= 1
            else :
                left_min -= 1
                left_max += 1
                if left_min < 0 :
                    left_min = 0
            if left_max < 0 :
                return False
        return (left_min == 0) or (left_max == 0 )


        
        """