class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = [[] for _ in range(n)]
        for fromi,to,wt in edges :
            adj[fromi].append((to,wt))
            adj[to].append((fromi,wt))
        count = [0]*n
        import heapq
        heap = []
        for src in range(n):
            dist = [float('inf')]*n
            dist[src] = 0
            heapq.heappush(heap,(0,src))   ## weight,node
            while heap :
                wt,node = heapq.heappop(heap)
                if wt >= distanceThreshold :
                    continue
                for nei,w in adj[node]:
                    if wt + w < dist[nei] :
                        dist[nei] = wt + w
                        heapq.heappush(heap,(wt+w,nei))
            for i in range(n):
                if dist[i] <= distanceThreshold :
                    count[src] += 1
        min_index = 0
        for i in range(n):
            if count[i] <= count[min_index]:
                min_index = i
        return min_index

            
            
        