class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10 or n >= 55 :
            return False
        
        i = 0
        while True :
            n = n - (10-i)
            if n < 0 :
                if i%2 == 0 :
                    return False
                else :
                    return True 
            i += 1


    
        