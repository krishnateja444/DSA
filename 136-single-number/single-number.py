class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        if len(nums) == 1 :
            return nums[0]
    
        nums.sort()
        for i in range(1,len(nums),2):
            if nums[i-1] != nums[i] :
                return nums[i-1]
        return nums[len(nums)-1]
                
         
        
        #for num in nums :
        #    if num not in l :
         #       return num
