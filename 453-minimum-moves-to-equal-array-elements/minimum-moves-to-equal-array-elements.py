
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        c = 0
        mini = min(nums)
        for i in range(len(nums)):
            c += nums[i] - mini
        return c



        """maxi = nums[-1]
        max_i = len(nums) - 1
        while True :
            if nums[0] == maxi :
                return c
            c += nums[max_i] - nums[0]
            nums[max_i] = nums[0]
            maxi = max(nums)
            max_i = nums.index(maxi)
        return c"""





        