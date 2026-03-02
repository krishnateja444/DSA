class Solution:
    def bsearch(self,nums,low,high,target):
        if low > high :
            return -1
        mid = (low + high)//2
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            return self.bsearch(nums,low,mid-1,target)
        if target > nums[mid]:
            return self.bsearch(nums,mid+1,high,target)
    def search(self, nums: List[int], target: int) -> int:
        return self.bsearch(nums,0,len(nums)-1,target)
       
        