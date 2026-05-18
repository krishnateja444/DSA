class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = [0 for i in range(len(nums))]
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0 :
                l[j] = nums[i]
                j = j + 1
        nums[:] = l[:]        
        