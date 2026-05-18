class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        if len(nums) == 1 :
            return nums[0]
        result = 0
        for i in range(len(nums)):
            result = result ^ nums[i]
        return result

                
         
        
        #for num in nums :
        #    if num not in l :
         #       return num
