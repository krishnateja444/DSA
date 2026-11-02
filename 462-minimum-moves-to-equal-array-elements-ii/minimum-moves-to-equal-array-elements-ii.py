class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        if n % 2 :
            mid = nums[n//2]
            ans = 0
            for num in nums :
                ans += abs(mid - num)
            return ans
        mid1 = nums[n//2-1]
        mid2 = nums[n//2]
        ans = 0
        for num in nums[:n//2]:
            ans += abs(mid1-num)
        for num in nums[n//2:]:
            ans += abs(mid2-num)
        ans += (n//2)*(mid2-mid1)
        return ans


        