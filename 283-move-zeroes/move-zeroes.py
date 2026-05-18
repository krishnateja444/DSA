class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0
        t = 0
        for i in range(len(nums)):
            if nums[i] == 0 :
                k += 1
            else :
                nums[t] = nums[i]
                t += 1
        nums[:] = nums[:t] + [0 for i in range(k)]

        