class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        if len(nums) == 0 :
            return 0
        for num in nums :
            d[num] = num
        max_l = 1
        curr = 0
        for key in d :
            if d[key] - 1 not in d and d[key] + 1 in d :
                x = d[key]
                while x in d :
                    curr += 1
                    x += 1
                max_l = max(max_l,curr)
                curr = 0
        return max_l



        