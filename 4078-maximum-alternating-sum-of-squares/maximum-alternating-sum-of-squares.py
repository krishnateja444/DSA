class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = sorted(nums, key = lambda x : abs(x))
        n = len(nums)
        ans = 0
        for i in range(n//2):
            ans += (nums[n-1-i]**2  - nums[i]**2)
        if n % 2 :
            ans += nums[n//2]**2
        return ans 

        