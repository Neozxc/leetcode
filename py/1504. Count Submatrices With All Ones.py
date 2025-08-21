class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0

        m, n = len(mat), len(mat[0])
        count = 0
        height = [0] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    height[j] += 1
                else:
                    height[j] = 0

            for j in range(n):
                if height[j] == 0:
                    continue

                min_h = height[j]

                for k in range(j, - 1, - 1):
                    min_h = min(min_h, height[k])

                    if min_h == 0:
                        break

                    count += min_h

        return count
