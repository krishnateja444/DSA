class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        left = min(bloomDay)
        right = max(bloomDay)
        def check(day):
            i = 0
            j = 0
            c = 0
            while i < len(bloomDay) :
                if bloomDay[i] <= day :
                    j += 1
                if bloomDay[i] > day :
                    j = 0
                if j == k :
                    c += 1
                    j = 0
                i += 1
            return c >= m
        ans = -1
        while left <= right :
            mid = (left + right)//2
            if check(mid) :
                ans = mid
                right = mid - 1
            else :
                left = mid + 1
        return ans
            
        



            
                    
        