class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in mp :
                return [i,mp[comp]]
            mp[nums[i]] = i
        

        