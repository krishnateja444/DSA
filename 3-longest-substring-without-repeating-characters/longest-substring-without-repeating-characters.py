class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s.strip()) == 0 :
            if s == "":
                return 0
            else :
                return 1
        left = 0
        max1 = 0
        s1 = set()
        for right in range(len(s)):
            while s[right] in s1 :
                s1.remove(s[left])
                left += 1
            max1 = max(right-left+1,max1)
            s1.add(s[right])
        return max1


        
        
        