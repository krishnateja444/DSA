class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*(n) for _ in range(m)]
        def dfs(i,j):
            visited[i][j] = True
            closed = ( i != 0 and i != m-1 and j != 0 and j!= n-1)
            dr = {(-1,0),(1,0),(0,-1),(0,1)}
            for x,y in dr :
                if 0 <= (i+x) < m and 0 <= (j+y) < n and grid[i+x][j+y] == 0 and not visited[i+x][j+y] :
                    nei_closed = dfs(i+x,j+y)
                    closed = closed and nei_closed
            return closed
        ans = 0
        for i in range(1,m-1):
            for j in range(1,n-1):
                if grid[i][j] == 0 and not visited[i][j] :
                    if dfs(i,j):
                        print(i,j)
                        ans += 1
        return ans 
        
        