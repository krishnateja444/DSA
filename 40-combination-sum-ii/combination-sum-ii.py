class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        l = []
        def backtrack(curr_sum,i):
            if curr_sum == target :
              
                res.append(l[:])
                return
            if i >= len(candidates) or curr_sum > target :
                return
            for j in range(i,len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                l.append(candidates[j])
            #backtrack(curr_sum + candidates[i],i)
    
                backtrack(curr_sum+candidates[j],j+1)
                l.pop()
                #backtrack(curr_sum,i+1)
        backtrack(0,0)
        return res
        