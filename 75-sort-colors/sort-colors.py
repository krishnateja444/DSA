class Solution:
    def qsort(self,l,low,high):
        if low >= high :
            return
        p = l[low]
        high_p = low + 1
        for i in range(low+1,high+1):
            if l[i] < p :
                l[i] , l[high_p] = l[high_p] , l[i]
                high_p += 1
        l[low] , l[high_p-1] = l[high_p-1] , l[low]
        self.qsort(l,low,high_p - 2)
        self.qsort(l,high_p,high)

    def sortColors(self, nums: List[int]) -> None:
        self.qsort(nums,0,len(nums)-1)
        return nums
        

       
        
        