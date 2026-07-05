class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_l = 0
        def expand_from_centre(left,right):
            nonlocal start,max_l
            while left >= 0 and right < len(s) and s[left] == s[right] :
                left -= 1
                right += 1
            length = right - left - 1
            if length > max_l :
                max_l = length
                start = left + 1
            return
        for i in range(len(s)):
            expand_from_centre(i,i)  ## odd
            expand_from_centre(i,i+1) ## even
        return s[start : max_l + start ]