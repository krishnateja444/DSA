class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        for u,v,w in times :
            adj[u].append((v,w))  ## target node,time
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        import heapq
        heap = []
        heapq.heappush(heap,(0,k))  ## time,node
        max_time = -1
        while heap :
            time,node = heapq.heappop(heap)
            for nei,t in adj[node]:
                if time + t < dist[nei] :
                    dist[nei] = time + t
                    heapq.heappush(heap,(time+t,nei))
        for i in range(1,n+1):
            if dist[i] == float('inf'):
                return -1
        dist[0] = 0
        return max(dist)




        