class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0 :
            nums1[:] = nums2
            return
        k = m
        for num in nums2 :
            nums1[k] = num
            k += 1
        nums1.sort()





        """
        Do not return anything, modify nums1 in-place instead.
        """
        