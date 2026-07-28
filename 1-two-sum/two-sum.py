class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)) :
            num = nums[i]
            if target - num in m :
                return [m[target-num],i]
            if num not in m :
                m[num] = i
        
        

        