class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diagonals = defaultdict(list)

        for r in range(n):
            for c in range(n):
                diagonals[r - c].append(grid[r][c])

        for key in diagonals:
            if key >= 0:
                diagonals[key].sort(reverse=True)
            else:
                diagonals[key].sort()

        pointers = defaultdict(int)

        for r in range(n):
            for c in range(n):
                key = r - c

                grid[r][c] = diagonals[key][pointers[key]]
                pointers[key] += 1

        return grid
