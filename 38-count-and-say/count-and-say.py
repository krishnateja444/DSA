class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1 :
            return '1'

        def cns(n):
            if n == 2 :
                return '11'
            prev = cns(n-1)
            ans = []
            c = 1
            for i in range(1,len(prev)): 
                if prev[i-1] == prev[i] :
                    c += 1
                else :
                    #ans += str(c) + prev[i-1]
                    ans.append(c)
                    ans.append(prev[i-1])
                    c = 1
            
            #ans += str(c) + prev[-1]
            ans.append(c)
            ans.append(prev[-1])
            return ''.join(map(str,ans))
        return cns(n)




        