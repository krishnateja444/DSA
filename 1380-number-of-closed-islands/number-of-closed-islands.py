class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(i,j):
            grid[i][j] = 1
            dr = [(-1,0),(1,0),(0,1),(0,-1)]
            for x,y in dr :
                nr = i + x
                nc = j + y
                if 0<= nr < m-1 and 0 <= nc < n-1 and grid[nr][nc] == 0 :
                    dfs(nr,nc)
        for j in range(n):
            if grid[0][j] == 0 :
                dfs(0,j)
            if grid[m-1][j] == 0 :
                dfs(m-1,j)
        for i in range(m):
            if grid[i][0] == 0 :
                dfs(i,0)
            if grid[i][n-1] == 0 :
                dfs(i,n-1)
        ans = 0
        for i in range(1,m-1):
            for j in range(1,n-1):
                if grid[i][j] == 0 :
                    dfs(i,j)
                    ans += 1
        return ans
