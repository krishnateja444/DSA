class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        if len(nums) == 0 :
            return 0
        num_set = set(nums)
        max_l = 1
        curr = 0
        for num in num_set :
            x = num
            curr = 0
            if num - 1 not in num_set and num + 1 in num_set :
                
                while x in num_set :
                    curr += 1
                    x += 1
                max_l = max(max_l,curr)
        return max_l



        