class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if s == t :
            return True
        d = {}
        l = []
        for i in range(len(s)):
            if s[i] not in d :
                if t[i] not in l :
                    d[s[i]] = t[i]
                    l.append(t[i])
                else :
                    return False

            else :
                if d[s[i]] != t[i] :
                    return False
        return True




        