class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        from collections import deque
        q = deque()
        dist = [[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0 :
                    dist[i][j] = 0
                    q.append((i,j,0))
        while q :
            i,j,t = q.popleft()
            if i > 0 and dist[i-1][j] == -1  :
                dist[i-1][j] = t + 1
                q.append((i-1,j,t+1))
                
            if i < m-1 and dist[i+1][j] == -1 :
                dist[i+1][j] = t + 1
                q.append((i+1,j,t+1))
                
            if j > 0 and dist[i][j-1] == -1 :
                dist[i][j-1] = t + 1
                q.append((i,j-1,t+1))
                
            if j < n-1 and dist[i][j+1] == -1 :
                dist[i][j+1] = t + 1
                q.append((i,j+1,t+1))
                
        return dist