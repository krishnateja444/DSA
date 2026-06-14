class Solution:
    def numEnclaves(self, board: List[List[int]]) -> int:
        m = len(board)
        n = len(board[0])
        #visited = [[False]*n for _ in range(m)]
        def dfs(i,j):
            #visited[i][j] = True
            board[i][j] = '#'
            if i > 0 and board[i-1][j] == 1 :
                dfs(i-1,j)
            if i < m-1 and board[i+1][j] == 1 :
                
                dfs(i+1,j)
            if j > 0 and board[i][j-1] == 1 :
                
                dfs(i,j-1)
            if j < n-1 and board[i][j+1] == 1 :
                
                dfs(i,j+1)
        for i in range(m):
            if board[i][0] == 1 :
                dfs(i,0)
            if board[i][n-1] == 1 :
                dfs(i,n-1)
        for j in range(n):
            if board[0][j] == 1 :
                dfs(0,j)
            if board[m-1][j] == 1 :
                dfs(m-1,j)
        res = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1 :
                    res += 1
        return res
         
        