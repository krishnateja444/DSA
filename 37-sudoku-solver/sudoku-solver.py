class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subgrids = [set() for _ in range(9)]
        for a in range(9):
            for b in range(9):
                if board[a][b] != '.' :
                    rows[a].add(board[a][b])
                    cols[b].add(board[a][b])
                    box = (a // 3) * 3 + (b // 3)
                    subgrids[box].add(board[a][b])
        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.' :
                        for c in "123456789":
                            if isvalid(board,i,j,c) :
                                board[i][j] = c
                                rows[i].add(c)
                                cols[j].add(c)
                                box = (i//3)*3 + (j//3)
                                subgrids[box].add(c) 
                                if solve(board):
                                    return True
                                else :
                                    board[i][j] = "."
                                    rows[i].remove(c)
                                    cols[j].remove(c)
                                    box = (i//3)*3 + (j//3)
                                    subgrids[box].remove(c) 
                        return False
            return True
        def isvalid(board,i,j,c):
            if c in rows[i]:
                return False
            if c in cols[j] :
                return False
            if c in subgrids[3*(i//3)+j//3] :
                return False
            return True
        solve(board)
                            
                
        
        