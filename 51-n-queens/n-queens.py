class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.']*n for _ in range(n)]
        def issafe(row, col):
            # columns
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            # upper-left
            i, j = row-1, col-1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # upper-right
            i, j = row-1, col+1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True
        def bt(row):
            if row == n :
                final = [''.join(row) for row in board]
                ans.append(final[:])
                return
            for col in range(n):
                board[row][col] = 'Q'
                if not issafe(row,col):
                    board[row][col] = '.'    
                else :
                    bt(row+1)
                    board[row][col] = '.'
        bt(0)
        return ans
        