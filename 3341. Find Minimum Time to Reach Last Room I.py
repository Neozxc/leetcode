class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        heap = [(0, 0, 0)]
        visited = [[float('inf')] * m for _ in range(n)]
        visited[0][0] = 0

        directions = [(-1, 0), (1, 0), (0, - 1), (0, 1)]

        while heap:
            time, r, c = heapq.heappop(heap)

            if r == n - 1 and c == m - 1:
                return time

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < m:
                    next_time = max(time, moveTime[nr][nc]) + 1

                    if next_time < visited[nr][nc]:
                        visited[nr][nc] = next_time
                        heapq.heappush(heap, (next_time, nr, nc))
