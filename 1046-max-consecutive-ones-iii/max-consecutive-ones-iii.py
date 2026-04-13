class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
            left = 0
            count_zero = 0
            max_count = 0
            for right in range(len(nums)):
                if nums[right] == 0 :
                    count_zero += 1
                while count_zero > k :
                    if nums[left] == 0 :
                        count_zero -= 1
                    left += 1
                max_count = max(right-left+1,max_count)
            return max_count


        