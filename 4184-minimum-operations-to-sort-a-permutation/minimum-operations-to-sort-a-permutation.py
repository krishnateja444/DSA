class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1,n):
            if abs(nums[i] - nums[i-1]) == 1 :
                continue
            else :
                if not (min(nums[i],nums[i-1])==0 and max(nums[i],nums[i-1])==n-1):
                    return -1
        need = len(nums)
        asc = False
        dec = False
        c = 1
        index = 0
        for i in range(1,2*n):
            if abs(nums[i%n] - nums[(i-1)%n]) == 1 :
                c += 1
                if c == need :
                    if nums[i%n] > nums[(i-1)%n] :
                        asc = True
                        index = i
                        break
                    else :
                        dec = True
                        index = i
                        break
            else :
                c = 1
        index += 1
        index %= n
        
        if asc :
            return min(index,n-index+2)
        if dec :
            return min(n - index +1,index+1)
        if nums[0] == 0 :
            return 0
        return 1
        




         