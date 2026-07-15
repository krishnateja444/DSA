class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(a,b):
            while b :
                a,b = b, a%b
            return a
        a = n**2
        b = n*(n+1)
        return gcd(a,b)
        