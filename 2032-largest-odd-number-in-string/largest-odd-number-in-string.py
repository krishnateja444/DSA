class Solution:
    def largestOddNumber(self, num: str) -> str:
        if int(num[-1]) % 2 != 0 :
            return num
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) % 2 != 0 :
                break
        if i == 0 and int(num[i]) %2 == 0 :
            return ""
        else :
            return num[:i+1]
        

        