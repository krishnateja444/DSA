class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = set()
        curr = 0
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i] :
                continue
            target = -nums[i]
            mp = {}
            for j in range(i+1,len(nums)):
                curr = nums[j]
                comp = target - curr
                if comp in mp :
                    ans.add((-target,comp,curr))
                if curr not in mp :
                    mp[curr] = i
        return [list(x) for x in ans]




        