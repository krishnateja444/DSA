class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        if n == 1 :
            return True
        min_odd = float('inf')
        for num in nums1 :
            if num % 2 != 0 and (num < min_odd) :
                min_odd = num 
        def solve(par):
            for i in range(len(nums1)):
                if nums1[i] % 2 == par :
                    continue
                else :
                    if (nums1[i] - min_odd < 1) :
                        return False
            return True
        return solve(0) or solve(1)
        
                         
        


        