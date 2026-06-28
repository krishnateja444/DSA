class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        total_cables = len(connections)
        if n-1 > total_cables :
            return -1
        adj = [[] for _ in range(n)]
        for u,v in connections :
            adj[u].append(v)
            adj[v].append(u)
        total = 0
        visited = [False]*n
        from collections import deque
        components = 0
        for i in range(n):
            if not visited[i]:
                components += 1
                q = deque([i])
                while q:
                    node = q.popleft()
                    if visited[node]:
                        continue

                    visited[node] = True

                    for nei in adj[node]:
                        if not visited[nei]:
                            q.append(nei)
        return components - 1