class Solution:
    def minOperations(self, s: str) -> int:
        l = list(s)
        #req = sorted(l)
        for i in range(1, len(s)):
            if s[i - 1] > s[i]:
                break
        else:
            return 0
        mini = min(l)
        maxi = max(l)
        if mini == s[0] or maxi == s[-1] :
            return 1
        if mini in s[:-1] or maxi in s[1:] :
            return 2
        if len(s) == 2 :
            return -1
        return 3