class Solution:
    def maxSubArray(self, nums: List[int]):
        max_sum = nums[0]
        s1 = nums[0]
        for i in range(1,len(nums)):
            s1 = max(nums[i],nums[i]+s1)
            max_sum = max(max_sum,s1)
        return max_sum 

        