class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def f(ind,tar):
            if ((ind,tar)) in dp :
                return dp[(ind,tar)]
            if ind == 0 :
                if tar == 0 and nums[ind] == 0 :
                    dp[(ind,tar)] = 2
                    return 2
                if nums[0] == tar or -nums[0] == tar :
                    dp[(ind,tar)] = 1
                    return 1
                dp[(ind,tar)]= 0
                return 0
            pos = f(ind-1,tar-nums[ind])
            neg = f(ind-1,tar+nums[ind])
            dp[(ind,tar)] = pos + neg
            return dp[(ind,tar)]
        return f(len(nums)-1,target)

        