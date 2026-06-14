class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = [[False]*n for _ in range(m)]
        def dfs(i,j):
            visited[i][j] = True
            if i > 0 and board[i-1][j] == 'O' :
                if not visited[i-1][j] :
                    dfs(i-1,j)
            if i < m-1 and board[i+1][j] == 'O' :
                if not visited[i+1][j] :
                    dfs(i+1,j)
            if j > 0 and board[i][j-1] == 'O' :
                if not visited[i][j-1] :
                    dfs(i,j-1)
            if j < n-1 and board[i][j+1] == 'O' :
                if not visited[i][j+1] :
                    dfs(i,j+1)
        for i in range(m):
            if board[i][0] == 'O' :
                dfs(i,0)
            if board[i][n-1] == 'O' :
                dfs(i,n-1)
        for j in range(n):
            if board[0][j] == 'O' :
                dfs(0,j)
            if board[m-1][j] == 'O' :
                dfs(m-1,j)
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and board[i][j] == 'O' :
                    board[i][j] = 'X'
         
        