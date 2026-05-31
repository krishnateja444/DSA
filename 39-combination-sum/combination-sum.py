class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        l1 = []
        def indiv(curr_sum,j):
            if curr_sum == target :
                res.append(l1[:])
                return
            if j >= len(candidates) or curr_sum > target :
                return
            
            l1.append(candidates[j])
            indiv(curr_sum + candidates[j],j)
            l1.pop()
            indiv(curr_sum,j + 1)
        indiv(0,0)
        return res


        
        