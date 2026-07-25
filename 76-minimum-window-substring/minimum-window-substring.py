class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) :
            return ""
        d = {}
        l = 0
        r  = 0
        for ch in s :
            if ch not in d :
                d[ch] = 0
        for ch in t :
            if ch not in d :
                return ""
            d[ch] += 1
        mini = 10**5
        min_i = -1
        ans = ""
        count = 0
        while l <= r and r < len(s):
            if count < len(t):
                if d[s[r]] > 0 :
                    count += 1
                d[s[r]] -= 1
            while count == len(t) :
                if mini > r - l + 1 :
                    mini = r - l + 1
                    min_i = l
                if d[s[l]] == 0 :
                    count -= 1
                d[s[l]] += 1
                l += 1
            r += 1
        if min_i == -1 :
            return ""
        return s[min_i:min_i+mini]



