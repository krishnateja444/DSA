class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        #mini = min(nums)
        mini_ind = [0]*(len(nums))
        mini_ind[-1] = nums[-1]
        maxi = nums[0]
        l = 0
        for i in range(len(nums)-2,-1,-1):
            mini_ind[i] = min(nums[i],mini_ind[i+1])
        while l < len(nums):
            maxi = max(maxi,nums[l])
            if maxi - mini_ind[l] <= k :
                return l
            l += 1
        return -1

        