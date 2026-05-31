class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(s,open_c,closed_c):
            if open_c == closed_c == n :
                res.append(s)
                return
            if open_c < n :
                s += '('
                backtracking(s,open_c+1,closed_c)
                s = s[:-1]
            if closed_c < open_c :
                s += ')'
                backtracking(s,open_c,closed_c + 1)
                s = s[:-1]
        backtracking("",0,0)
        return res

        
        


        


        