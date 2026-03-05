class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        if len(nums) == 1 :
            return nums[0]
        l = []
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i] :
                l.append(nums[i])
        k = sum(nums) - 2*sum(l)
        return k
                
         
        
        #for num in nums :
        #    if num not in l :
         #       return num
