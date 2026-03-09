class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        d1 = {}
        for i in range(len(s)):
            if s[i] not in d1 :
                d1[s[i]] = 1
            else :
                d1[s[i]] += 1
            if t[i] not in d1 :
                d1[t[i]] = -1
            else :
                d1[t[i]] -= 1
        for i in s :
            if d1[i] != 0 :
                return False
        return True
            


        