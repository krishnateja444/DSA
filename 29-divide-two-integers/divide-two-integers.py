class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        q = 0
        sign = True  
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if dividend == -2**31 and divisor == 1:
            return - (2**31 )    

        if dividend == divisor :
            return 1
        if (dividend >= 0 and divisor < 0):
            sign = False
        if (dividend <= 0 and divisor > 0):
            sign = False
        n , d = abs(dividend) , abs(divisor) 
        while n >= d :
            i = 0 
            while (n >= (d << (i+1 ))) :
                i += 1
            q += 1 << i
            n = n - (d << i)
        if q > (2**31 - 1)  :
            return 2**31 - 1
        if q < -(2)**31 :
            return -(2)**31
        if sign :
            return q  
        return -q     

