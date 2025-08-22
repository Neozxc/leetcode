class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        top_r = float('inf')
        bot_r = float('-inf')
        left_c = float('inf')
        right_c = float('-inf')

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    top_r = min(top_r, r)
                    bot_r = max(bot_r, r)
                    left_c = min(left_c, c)
                    right_c = max(right_c, c)

        height = bot_r - top_r + 1
        width = right_c - left_c + 1

        return height * width
