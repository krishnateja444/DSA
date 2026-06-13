class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        from collections import deque
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2 :
                    q.append((i,j,0))
        max_time = 0
        while q :
            i,j,t = q.popleft()
            if i > 0 and grid[i-1][j] == 1 :
                grid[i-1][j] = 2
                q.append((i-1,j,t+1))
                max_time = max(max_time,t+1)
            if i < m-1 and grid[i+1][j] == 1 :
                grid[i+1][j] = 2
                q.append((i+1,j,t+1))
                max_time = max(max_time,t+1)
            if j > 0 and grid[i][j-1] == 1 :
                grid[i][j-1] = 2
                q.append((i,j-1,t+1))
                max_time = max(max_time,t+1)
            if j < n-1 and grid[i][j+1] == 1 :
                grid[i][j+1] = 2
                q.append((i,j+1,t+1))
                max_time = max(max_time,t+1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 :
                    return -1
        return max_time

        