class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]
        prev_max = nums[0]
        prev_min = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)) :
            if nums[i] < 0 :
                prev_max,prev_min = prev_min,prev_max
            curr_max = max(nums[i],prev_max*nums[i],prev_min*nums[i])
            curr_min = min(nums[i],prev_min*nums[i],prev_max*nums[i])
            prev_max,prev_min = curr_max,curr_min
            ans = max(ans,prev_max)
        return ans
           