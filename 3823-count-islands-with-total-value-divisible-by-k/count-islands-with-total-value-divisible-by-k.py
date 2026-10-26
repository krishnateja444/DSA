class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(i,j):
            ans = grid[i][j]
            grid[i][j] = 0
            dr = [(-1,0),(1,0),(0,-1),(0,1)]
            for x,y in dr :
                nr = i + x
                nc = j + y
                if 0<= nr < m and 0<= nc < n and grid[nr][nc] != 0 :
                    ans += dfs(nr,nc)
            return ans
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and dfs(i,j)%k == 0 :
                    res += 1
        return res
        