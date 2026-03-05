class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_index = 0
        for num in nums :
            max_index = nums.index(max(nums[max_index],num))
        return max_index


        