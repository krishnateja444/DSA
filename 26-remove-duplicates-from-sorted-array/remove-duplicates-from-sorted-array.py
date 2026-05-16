class Solution:
    def removeDuplicates(self,nums):
        d1 = {}
        for i in range(len(nums)) :
            if nums[i] not in d1 :
                d1[nums[i]] = 1
            else :
                d1[nums[i]] += 1
        k = 0
        for key in d1 :
            nums[k] = key
            k += 1
        return k  
          

        