class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        """res = [['#']*(n) for _ in range(m)]
        for i in range(n):
            res[0][i] = '.'
        for j in range(m):
            res[j][-1] = '.'
        return res"""
        row = '#'*(n-1) + '.'
        first_row = '.'*(n)
        res = [row for _ in range(m-1)]
        res = [first_row] + res
        return res
            