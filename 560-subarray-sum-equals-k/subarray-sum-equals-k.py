class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = 0
        mp = {}
        count = 0
        for i in range(n):
            prefix_sum += nums[i]
            comp = prefix_sum - k
            if comp in mp :
                count += mp[comp]
            if prefix_sum == k :
                count += 1
            if prefix_sum not in mp :
                mp[prefix_sum] = 1
            else :
                mp[prefix_sum] += 1
        return count
