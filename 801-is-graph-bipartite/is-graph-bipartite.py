class Solution:
    def isBipartite(self, adj: List[List[int]]) -> bool:
        n = len(adj)
        ans = [-1]*(n)
        from collections import deque
        for start in range(n):
            if ans[start] != -1 :
                continue
            q = deque()
            q.append((start,0))
            ans[start] = 0
        #visited = [False]*(n)
            while q :
                node,c = q.popleft()
            #visited[node] = True
                for nei in adj[node]:
                    if ans[nei] == c :
                        return False
                    if ans[nei] == -1 :
                        ans[nei] = 1- c
                        q.append((nei,1 - c))
        return True
