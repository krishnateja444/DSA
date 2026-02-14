class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0 :
            return False
        if n == 1 :
            return True
        if n %2 != 0 :
            return False    
        i = 0    
        while (1 << i) <= n:
            if (n ^ (1<<i) == 0):
                return True
            i += 1
        return False        
                    
        