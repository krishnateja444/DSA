class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0 :
            return -1
        dist = [[float('inf')]*n for _ in range(n)]
        dist[0][0] = 0
        from collections import deque
        q = deque()
        q.append((0,0,0)) ## (dist,row,col)
        directions = [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1),  (1, 0),  (1, 1)]
        while q:
            d, r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0):
                    if d + 1 < dist[nr][nc]:
                        dist[nr][nc] = d + 1
                        q.append((dist[nr][nc], nr, nc))
        if dist[n-1][n-1] == float('inf'):
            return -1
        return dist[n-1][n-1] + 1

        