class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        temp = []
        for i,num in enumerate(nums) :
            temp.append((sum(int(d) for d in str(num)),num,i))
        temp.sort()
        perm = [arr[2] for arr in temp]
        visited = [False]*(len(nums))
        swaps = 0
        
        for i in range(len(nums)):
            cycle_len = 0
            if i == perm[i] or visited[i] :
                continue
            j = i
            while not visited[j] :
                visited[j] = True
                j = perm[j]
                cycle_len += 1
            swaps += cycle_len - 1
        return swaps


        
        