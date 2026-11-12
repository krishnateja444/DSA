class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxi = 1
        p = -1
        c = 1
        for i in range(1,len(nums)):
            if p == -1 :
                if nums[i] > nums[i-1] :
                    p = 1
                
                elif nums[i] < nums[i-1] :
                    p = 0
                else :
                    c = 0
            elif p == 1 :
                if nums[i] < nums[i-1]:
                    p = 0
                    c = 1
                elif nums[i] == nums[i-1] :
                    p = -1
                    c = 0
            else :
                if nums[i] > nums[i-1]:
                    p = 1
                    c = 1
                elif nums[i] == nums[i-1] :
                    p = -1
                    c = 0
            c += 1
            maxi = max(maxi,c)
        return maxi


                


        