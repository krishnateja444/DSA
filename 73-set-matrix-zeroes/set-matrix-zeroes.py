class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        row_zero = False
        column_zero = False
        for j in range(len(m[0])):
            if m[0][j] == 0 :
                row_zero = True
            
        for i in range(len(m)):
            if m[i][0] == 0 :
                column_zero = True
        for i in range(1,len(m)):
            for j in range(1,len(m[0])):
                if m[i][j] == 0 :
                    m[0][j] = 0
                    m[i][0] = 0
        
        for i in range(1,len(m)):
            if m[i][0] == 0 :
                for j in range(len(m[0])):
                    m[i][j] = 0
        for j in range(1,len(m[0])):
            if m[0][j] == 0 :
                for i in range(len(m)):
                    m[i][j] = 0
        if row_zero :
            for i in range(len(m[0])):
                m[0][i] = 0
        if column_zero :
            for j in range(len(m)):
                m[j][0] = 0
        return m