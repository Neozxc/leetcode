class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        count = 0

        for j in range(n):
            x_j, y_j = points[j]
            min_y_blocker = float('inf')

            for i in range(j - 1, - 1, - 1):
                x_i, y_i = points[i]

                if y_i >= y_j:
                    if y_i < min_y_blocker:
                        count += 1

                    min_y_blocker = min(min_y_blocker, y_i)

        return count
