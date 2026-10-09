class Solution:
    def minInsertions(self, s: str) -> int:
        l_c = 0
        ans = 0
        i = 0
        while i < len(s):
            ch = s[i]
            if ch == '(':
                l_c += 1
            else :
                if i < len(s) - 1 :
                    if s[i+1] == s[i] :
                        if l_c > 0 :
                            l_c -= 1
                        else :
                            ans += 1
                        i += 1
                    else :
                        ans += 1
                        if l_c <= 0 :
                            ans += 1
                        else :
                            l_c -= 1
                else:
                    ans += 1
                    if l_c > 0 :
                        l_c -= 1
                    else :
                        ans += 1
            i += 1

        return ans + 2*l_c

                    


        