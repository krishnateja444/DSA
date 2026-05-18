class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k > len(nums) :
            k = k % len(nums)
        n = len(nums)
        nums[:] = nums[n-k:] + nums[:n-k]


            
        