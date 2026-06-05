class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        if k == n :
            return total
        window = n - k
        curr = sum(cardPoints[:window])
        min_sum = curr
        for i in range(window,n):
            curr += cardPoints[i]
            curr -= cardPoints[i - window]
            min_sum = min(curr,min_sum)
        return total - min_sum


                
        

            
        



        