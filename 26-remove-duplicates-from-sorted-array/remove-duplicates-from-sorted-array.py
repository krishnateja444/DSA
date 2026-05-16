class Solution:
    def removeDuplicates(self,nums):
        l = []
        for i in nums :
            if i not in l :
                l.append(i)
        k = len(l)
        for i in range(k):
            nums[i] = l[i]
        return k    
          

        