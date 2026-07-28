class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1 :
            return s
        d = {}
        for ch in s :
            if ch not in d:
                d[ch] = 1
            else :
                d[ch] += 1
        d = {k:v for k,v in sorted(d.items())}
        ans = []
        l = 0
        mid = ""
        for key in d :
            if d[key] % 2 :
                mid = key
             
            ans.append(key*(d[key]//2))
        ans = "".join(ans)
        return ans + mid + ans[::-1]



        


        