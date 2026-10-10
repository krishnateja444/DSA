class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        freq = [0]*(100001)
        max_diff = 0
        total_diff = 0
        k = k1 + k2
        for n1,n2 in zip(nums1,nums2):
            t = abs(n1-n2)
            freq[t] += 1
            max_diff = max(max_diff,t)
            total_diff += t
        if total_diff <= k :
            return 0
        for j in range(max_diff,0,-1):
            if k == 0 :
                break
            moves = min(k,freq[j])
            freq[j] -= moves
            freq[j-1] += moves
            k -= moves
        ans = 0
        for j in range(max_diff,0,-1):
            ans += ((j*j)*freq[j])
        return ans