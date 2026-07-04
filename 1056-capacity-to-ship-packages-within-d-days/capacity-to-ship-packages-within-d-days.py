class Solution:
    def shipWithinDays(self, w: List[int], days: int) -> int:
        n = len(w)
        right = sum(w)
        left = max(w)
        def check(wt):
            j = 0
            i = 0
            d = 1
            while i < len(w) :
                #j += w[i]
                if j + w[i] > wt :
                    d += 1
                    j = w[i]
                else :
                    j += w[i]
                i += 1
            return d
        ans = right
        while left <= right :
            mid = (left + right)//2
            val = check(mid)
            if val <= days :
                ans = mid
                right = mid - 1
            else :
                left = mid + 1
        return ans




        