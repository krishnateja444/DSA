class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0 :
            return -1
        from collections import deque
        q = deque()
        q.append((0,0,0)) ## (dist,row,col)
        grid[0][0] = 1
        directions = [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1),  (1, 0),  (1, 1)]
        while q:
            d, r, c = q.popleft()
            if r == n-1 and c == n-1:
                return d + 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0):
                    grid[nr][nc] = 1
                    q.append((d + 1, nr, nc))
        return -1

        