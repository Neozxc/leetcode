class FTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)


    def update(self, index, delta):
            index += 1

            while index < len(self.tree):
                self.tree[index] += delta
                index += index & (-index)

    def query(self, index):
        index += 1
        s = 0

        while index > 0:
            s += self.tree[index]
            index -= index & (-index)

        return s

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        count = 0

        max_y = 50

        for i in range(n):
            a_x, a_y = points[i]

            ft = FTree(max_y + 1)

            for j in range(i + 1, n):
                b_x, b_y = points[j]

                if a_y >= b_y:
                    count_in_range = ft.query(a_y) - ft.query(b_y - 1)

                    if count_in_range == 0:
                        count += 1

                ft.update(b_y, 1)

        return count
