class Solution:
    def minSwaps(self, s: str) -> int:
        sc = 0
        min_bal = 0
        for ch in s :
            if ch == '[' :
                sc += 1
            else :
                sc -= 1
                if sc < 0:
                    min_bal = min(min_bal,sc)
        return (-min_bal + 1 ) // 2
        