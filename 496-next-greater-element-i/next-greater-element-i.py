class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}
        for num in nums2 :
            while stack and num > stack[-1]:
                d[stack.pop()] = num
            stack.append(num)
        for num in stack :
            d[num] = -1
        stack = []
        for num in nums1 :
            stack.append(d[num])
        return stack
