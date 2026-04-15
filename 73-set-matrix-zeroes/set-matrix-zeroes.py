class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        rows = set()
        columns = set()
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] == 0 :
                    rows.add(i)
                    columns.add(j)
        for i in rows :
            for j in range(len(m[0])):
                m[i][j] = 0
        for j in columns :
            for k in range(len(m)):
                m[k][j] = 0
        
        