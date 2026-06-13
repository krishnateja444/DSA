class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False]*(len(isConnected))
        count = 0
        def dfs(adj_m, v):
            visited[v] = True
            for i in range(len(adj_m)):
                if not visited[i] and adj_m[v][i] == 1 :
                    dfs(adj_m,i)
        for i in range(len(isConnected)):
            if not visited[i] :
                dfs(isConnected,i)
                count += 1
        return count
    
        