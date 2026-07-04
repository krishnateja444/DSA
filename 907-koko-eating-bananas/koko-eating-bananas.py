import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi = max(piles)
        def req_time(x):
            t = 0
            for i in range(len(piles)):
                t += math.ceil(piles[i]/x)
            return t
        left = 1
        ans = 0
        right = maxi
        while left <= right :
            mid = (left + right)//2
            if req_time(mid) <= h :
                ans = mid
                right = mid - 1
            else :
                left = mid + 1
        return ans

