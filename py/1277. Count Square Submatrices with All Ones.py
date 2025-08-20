class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        count = 0

        if m == 0:
            return 0

        for i in range(m):
            count += matrix[i][0]

        for j in range(n):
            count += matrix[0][j]

        if matrix[0][0] == 1:
            count -= 1

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    side = 1 + min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1])
                    matrix[i][j] = side
                    count += side

        return count
