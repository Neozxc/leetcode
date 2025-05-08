class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        dist = [[[float('inf')] * 2 for _ in range(m)] for __ in range(n)]

        dist[0][0][0] = 0
        heap = [(0, 0, 0, 0)]

        directions = [(-1, 0), (1, 0), (0, - 1), (0, 1)]

        while heap:
            time, r, c, p = heapq.heappop(heap)

            if time > dist[r][c][p]:
                continue

            if r == n - 1 and c == m - 1:
                return time

            move_cost = 1 if p == 0 else 2
            next_p = 1 - p

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < m:
                    start_when = max(time, moveTime[nr][nc])
                    arrival = start_when + move_cost

                    if arrival < dist[nr][nc][next_p]:
                        dist[nr][nc][next_p] = arrival
                        heapq.heappush(heap, (arrival, nr, nc, next_p))

        return - 1
