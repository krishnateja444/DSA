class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        visited = set()
        from collections import deque
        q = deque()
        q.append((1,0))
        visited.add(1)
        def helper(val):
            i = (val - 1) // n
            #val = val - n*i
            j = (val - 1)%n
            if i % 2 != 0 :
                j = n - j - 1
            i = n - i - 1
            return i,j
        while q :
            val,mini = q.popleft()
            i,j = helper(val)
            for nxt in range(val+1, min(val+6, n*n)+1):
                i,j = helper(nxt)
                if board[i][j] == -1 :
                    if nxt == n * n:
                        return mini + 1
                    if nxt not in visited :
                        visited.add(nxt)
                        q.append((nxt,mini+1))
                else :
                    if board[i][j] == n*n :
                        return mini + 1
                    if board[i][j] not in visited :
                        visited.add(board[i][j])
                        q.append((board[i][j],mini+1))
        return -1
        
            
        