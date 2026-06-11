class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_i = 0 # max_index
        for i in range(len(nums)):
            if max_i < i :
                return False
            max_i = max(max_i,i + nums[i])
        return True