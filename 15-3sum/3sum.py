class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        curr = 0
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i] :
                continue
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right :
                if nums[left] + nums[right] == target :
                    ans.append([nums[left],nums[right],-target])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1] :
                        left += 1
                    while left < right and nums[right+1] == nums[right]:
                        right -= 1
                elif nums[right] + nums[left] < target :
                    left += 1
                elif nums[right] + nums[left] > target :
                    right -= 1
        return ans

