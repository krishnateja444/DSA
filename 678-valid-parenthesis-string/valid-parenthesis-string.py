class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min = 0
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


        
        