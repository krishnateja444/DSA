class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_val = nums[0]
        ind = 0
        for i in range(len(nums)) :
            if nums[i] > max_val :
                ind = i
                max_val = nums[i]
        return ind
            


        