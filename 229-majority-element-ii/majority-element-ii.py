class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp = {}
        n = len(nums)
        ans = []
        for num in nums :
            if num not in mp :
                mp[num] = 1
            else :
                mp[num] += 1
        for num in mp :
            if mp[num] > n//3 :
                ans.append(num)
        return ans
                

        