class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        l = []
        nums.sort()
        def backtrack(l,i):
            if i >= len(nums):
                return
            l.append(nums[i])
            if l[:] not in res :
                res.append(l[:])
            backtrack(l,i+1)
            l.pop()
            backtrack(l,i+1)
        backtrack([],0)
        return res

            

        