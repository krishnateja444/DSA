class Solution:
    def check(self,nums):
        count = 0
        n = len(nums)
    
        for i in range(n-1):
            if nums[i] > nums[(i + 1)]:
                count += 1
        if nums[0] < nums[n-1]:
            count += 1
        return count <= 1         
        
        