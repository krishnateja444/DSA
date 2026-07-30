class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        import heapq
        dist = [[float('inf')]*(n) for _ in range(n)]
        heap = []
        heapq.heappush(heap,(grid[0][0],0,0))
        dist[0][0] = 0
        while heap :
            t,i,j = heapq.heappop(heap)
            if i == n-1 and j == n-1 :
                return t
            if i > 0 and dist[i-1][j] > max(t,grid[i-1][j]) :
                dist[i-1][j] = max(t,grid[i-1][j])
                heapq.heappush(heap,(dist[i-1][j],i-1,j))
            if i < n-1 and dist[i+1][j] > max(t,grid[i+1][j]) :
                dist[i+1][j] = max(t,grid[i+1][j])
                heapq.heappush(heap,(dist[i+1][j],i+1,j))
            if j < n-1 and dist[i][j+1] > max(t,grid[i][j+1]) :
                dist[i][j+1] = max(t,grid[i][j+1])
                heapq.heappush(heap,(dist[i][j+1],i,j+1))
            if j > 0 and dist[i][j-1] > max(t,grid[i][j-1]) :
                dist[i][j-1] = max(t,grid[i][j-1])
                heapq.heappush(heap,(dist[i][j-1],i,j-1))
                
            
        