class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if num*(9) < sum :
            return ""
        if sum < 10 :
            return str(sum) + "0"*(num-1)
        else :
            q = sum//9
            if sum%9 :
                res = '9'*(q) + str(sum%9)
            else :
                res = '9'*(q)
            res += '0'*(num-len(res))
        return res


        
        