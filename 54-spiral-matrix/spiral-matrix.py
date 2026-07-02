class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1
        ans = []
        while top <= bottom and left <= right :
            for i in range(left,right+1):
                ans.append(mat[top][i])
            top += 1
            for j in range(top,bottom+1):
                ans.append(mat[j][right])
            right -= 1
            if top <= bottom :
                for i in range(right,left-1,-1):
                    ans.append(mat[bottom][i])
                bottom -= 1
            if left <= right :
                for j in range(bottom,top-1,-1):
                    ans.append(mat[j][left])
                left += 1
        return ans