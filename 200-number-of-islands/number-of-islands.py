class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(i,j):
            visited[i][j] = True
            if i > 0 and grid[i-1][j] == '1' :
                if not visited[i-1][j] :
                    dfs(i-1,j)
            if i < m-1 and grid[i+1][j] == '1' :
                if not visited[i+1][j] :
                    dfs(i+1,j)
            if j > 0 and grid[i][j-1] == '1' :
                if not visited[i][j-1] :
                    dfs(i,j-1)
            if j < n-1 and grid[i][j+1] == '1' :
                if not visited[i][j+1] :
                    dfs(i,j+1)
        visited = [[False]*n for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i,j)
                    count += 1
        return count
                    

            
        