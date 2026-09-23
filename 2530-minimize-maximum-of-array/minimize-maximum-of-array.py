class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        maxi = 0
        prefix = 0
        for i,num in enumerate(nums):
            prefix += num
            maxi = max(maxi,(prefix + i)// (i+1))
        return maxi

        