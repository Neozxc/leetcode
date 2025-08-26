class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_dgn = -1
        max_area = 0

        for length, width in dimensions:
            diagonal_sq = length**2 + width**2

            if diagonal_sq > max_dgn:
                max_dgn = diagonal_sq
                max_area = length * width
            elif diagonal_sq == max_dgn:
                max_area = max(max_area, length * width)

        return max_area
