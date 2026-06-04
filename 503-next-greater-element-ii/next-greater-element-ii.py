class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1 for i in range(len(nums))]
        for i in range(2*len(nums)):
            num = nums[i % len(nums)]
            while stack and num > nums[stack[-1]]:
                ans[stack.pop()] = num
            if i < len(nums) :
                stack.append(i % len(nums))
        stack = []
        return ans


                

        