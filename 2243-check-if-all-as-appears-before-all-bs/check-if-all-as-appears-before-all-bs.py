class Solution:
    def checkString(self, s: str) -> bool:
        par = False
        for ch in s :
            if ch == 'a' and par :
                return False
            elif ch == 'b' :
                par = True
        return True
        
        