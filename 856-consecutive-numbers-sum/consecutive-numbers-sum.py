class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        cnt = 0
        p = 2
        while p * (p+1) // 2 <= n :
            rem = n -  p * (p+1)//2 
            if (rem)%(p) == 0 :
                cnt += 1
            p += 1
        return cnt + 1


        