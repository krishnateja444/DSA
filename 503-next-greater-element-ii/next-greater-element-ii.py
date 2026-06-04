class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        d = {}
        for i in range(len(nums)) :
            d[i] = -1
        for i in range(2*len(nums)):
            num = nums[i % len(nums)]
            while stack and num > nums[stack[-1]]:
                d[stack.pop()] = num
            stack.append(i % len(nums))
        stack = []
        for i in range(len(nums)) :
            stack.append(d[i])
        return stack


                

        