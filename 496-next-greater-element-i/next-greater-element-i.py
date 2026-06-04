class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d1 = {}
        for num in nums2 :
            d1[num] = -1
        i = 0
        j = 1
        while  i < len(nums2) :
            if j < len(nums2) and nums2[j] > nums2[i]  :
                d1[nums2[i]] = nums2[j] 
                i += 1
                j = i + 1   
            elif j >= len(nums2) :
                i += 1
                j = i + 1
            else :
                j += 1
        
        for num in nums1 :
            stack.append(d1[num])
        return stack
              