class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1
        while i > 0 :
            if nums[i-1] < nums[i] :
                break
            else :
                i -= 1
        if i == 0 :
            nums.reverse()
            return 
        for j in range(len(nums)-1,-1,-1):
            if nums[j] > nums[i-1] :
                nums[j],nums[i-1] = nums[i-1],nums[j]
                break
        nums[i:] = nums[i:][::-1]
        return 