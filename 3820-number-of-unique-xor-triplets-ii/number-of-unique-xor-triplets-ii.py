class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        s = set()
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                s.add(nums[i]^nums[j])
        s1 = set()
        for num in s :
            for i in range(len(nums)):
                s1.add(num^nums[i])

        return len(s1)
        