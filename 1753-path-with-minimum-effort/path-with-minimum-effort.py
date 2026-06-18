class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0

        import heapq

        heap = []
        heapq.heappush(heap, (0, 0, 0))  # effort,row,col

        while heap:

            diff, r, c = heapq.heappop(heap)

            if r == m - 1 and c == n - 1:
                return diff



            # Up
            if r > 0:
                new_diff = max(
                    diff,
                    abs(heights[r-1][c] - heights[r][c])
                )

                if new_diff < dist[r-1][c]:
                    dist[r-1][c] = new_diff
                    heapq.heappush(heap, (new_diff, r-1, c))

            # Down
            if r < m - 1:
                new_diff = max(
                    diff,
                    abs(heights[r+1][c] - heights[r][c])
                )

                if new_diff < dist[r+1][c]:
                    dist[r+1][c] = new_diff
                    heapq.heappush(heap, (new_diff, r+1, c))

            # Left
            if c > 0:
                new_diff = max(
                    diff,
                    abs(heights[r][c-1] - heights[r][c])
                )

                if new_diff < dist[r][c-1]:
                    dist[r][c-1] = new_diff
                    heapq.heappush(heap, (new_diff, r, c-1))

            # Right
            if c < n - 1:
                new_diff = max(
                    diff,
                    abs(heights[r][c+1] - heights[r][c])
                )

                if new_diff < dist[r][c+1]:
                    dist[r][c+1] = new_diff
                    heapq.heappush(heap, (new_diff, r, c+1))

        return 0