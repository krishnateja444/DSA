class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] == ')' or grid[m-1][n-1] == "(":
            return False
        #stack = []
        dp = {}
        def solve(i,j,l_c): # down = (i+1,j) right = (i,j+1)
            if i >= m or j >= n :
                return False
            if i == m-1 and j == n-1 :
                if not l_c :
                    return False
                l_c -= 1
                return not l_c
            new_lc = l_c
            if (i,j,l_c) in dp :
                return dp[(i,j,l_c)]
            if grid[i][j] == '(' :
                new_lc += 1
            elif l_c == 0 :
                dp[(i,j,l_c)] = False
                return False
            else :
                new_lc -= 1
            down = solve(i+1,j,new_lc)
            right = solve(i,j+1,new_lc)
            dp[(i,j,l_c)] = down or right
            return dp[(i,j,l_c)]
        return solve(0,0,0)

        