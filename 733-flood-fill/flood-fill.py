class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        from collections import deque
        q = deque()
        initial_color = image[sr][sc]
        image[sr][sc] = color
        if initial_color == color :
            return image
        q.append((sr,sc))
        while q :
            i,j = q.popleft()
            if i > 0 and image[i-1][j] == initial_color :
                image[i-1][j] = color
                q.append((i-1,j))
            if i < m-1 and image[i+1][j] == initial_color :
                image[i+1][j] = color
                q.append((i+1,j))
            if j > 0 and image[i][j-1] == initial_color :
                image[i][j-1] = color
                q.append((i,j-1))
            if j < n-1 and image[i][j+1] == initial_color :
                image[i][j+1] = color
                q.append((i,j+1))
        return image

        