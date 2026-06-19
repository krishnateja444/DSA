class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for fromi,to,price in flights :
            adj[fromi].append((to,price))
        if not adj[src] :
            return -1
        dist = [float('inf')]*n
        dist[src] = 0
        from collections import deque
        q = deque()
        q.append((0,0,src))  ##(stops,price,node)
        while q :
            st,pr,node = q.popleft()
            if st > k  :
                continue
            for nei,price in adj[node]:
                if pr + price < dist[nei] and st <= k :
                    dist[nei] = pr + price
                    q.append((st+1,pr+price,nei))
        if dist[dst] == float('inf'):
            return -1
        return dist[dst]


        