class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        if len(nums) == 1 :
            if target == nums[0] :
                return [0,0]
            return [-1,-1]
        ans = -1
        res = []
        while left <= right :
            mid = (left + right)//2
            if nums[mid] == target :
                ans = mid
                right = mid - 1
            if nums[mid] < target :
                left = mid + 1
            if nums[mid] > target :
                right = mid - 1
        res.append(ans)
        left = 0
        right = len(nums) - 1
        while left <= right :
            mid = (left + right)//2
            if nums[mid] == target :
                ans = mid
                left = mid + 1
            if nums[mid] < target :
                left = mid + 1
            if nums[mid] > target :
                right = mid - 1
        res.append(ans)
        return res

        