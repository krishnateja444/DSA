class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        mini = float('inf')
        maxi = float('-inf')
        stack = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                maxi = max(maxi,nums[j])
                mini = min(mini,nums[j])
                ans += (maxi - mini)
            maxi = float('-inf')
            mini = float('inf')
        return ans


        