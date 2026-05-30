class Solution:
    Mod = 10**9 + 7
    def pow(self,x,n):
        if n == 0 :
            return 1
        if n < 0 :
            return self.pow(1/x,-n)
        half = self.pow(x,n//2) 
        if n % 2 == 0 :
            return (half*half) % self.Mod
        else :
            return (half*half*x) % self.Mod
    def countGoodNumbers(self, n: int) -> int:
        if n == 1 :
            return 5
        val = self.pow(4,n//2) * self.pow(5,n//2)
        if n % 2 == 0 :
            return val % self.Mod
        else :
            return (val * 5 )% self.Mod

             
        