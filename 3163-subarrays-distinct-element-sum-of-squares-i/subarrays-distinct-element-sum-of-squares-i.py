class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        s = set()
        res = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                
                s.add(nums[j])
                res += len(s)**2
            s = set()
        return res
        