class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if n - 1 > len(connections) :
            return -1
        visited = [False]*(n)
        k = 0
        adj = [[] for _ in range(n)]
        for u,v in connections :
            adj[u].append(v)
            adj[v].append(u)
        def dfs(node):
            visited[node] = True
            for nei in adj[node]:
                if not visited[nei] :
                    dfs(nei)
        for i in range(n):
            if not visited[i]:
                dfs(i)
                k += 1
        return k - 1
             
