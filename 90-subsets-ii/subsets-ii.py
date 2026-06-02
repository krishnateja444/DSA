class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        l = []
        nums.sort()
        def backtrack(l,i):
            #if i >= len(nums):
             #   return
            for j in range(i,len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                l.append(nums[j])
                res.append(l[:])
                backtrack(l,j+1)
                l.pop()
        backtrack([],0)
        return res

            

        