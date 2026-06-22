class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        if total % 2 != 0 :
            return False
        target = total/2
        prev = [False]*(int(target)+1)
        if nums[0] <= int(target) :
            prev[nums[0]] = True
        for i in range(1,n):
            curr = [False]*(int(target)+1)
            prev[0] = curr[0] = True
            for j in range(1,int(target)+1):
                if nums[i] > j :
                    curr[j] = prev[j]
                else :
                    curr[j] = prev[j] or prev[j-nums[i]]
            prev = curr
        return prev[int(target)]
