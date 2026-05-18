class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        t = 0
        for i in range(len(nums)):
            if nums[i] != 0 :
                if i != t :
                    nums[t] = nums[i]
                t += 1
        for i in range(n-t):
            if t < len(nums):
                nums[t] = 0
                t = t + 1
        