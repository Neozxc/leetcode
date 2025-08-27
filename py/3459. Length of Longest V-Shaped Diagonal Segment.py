class Solution:
    def lenOfVDiagonal(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def get_expected_val(length):
            if length == 1:
                return 1
            return 2 if length % 2 == 0 else 0

        dp_in = collections.defaultdict(lambda: [[0] * m for _ in range(n)])
        dp_out = collections.defaultdict(lambda: [[0] * m for _ in range(n)])

        dirs = {
            "tlbr": (1, 1),
            "trbl": (1, -1),
            "bltr": (-1, 1),
            "brtl": (-1, -1),
        }

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dp_in["tlbr"][i][j] = 1
                elif i > 0 and j > 0:
                    prev_len = dp_in["tlbr"][i - 1][j - 1]
                    if prev_len > 0 and grid[i][j] == get_expected_val(prev_len + 1):
                        dp_in["tlbr"][i][j] = prev_len + 1
        for i in range(n):
            for j in range(m - 1, -1, -1):
                if grid[i][j] == 1:
                    dp_in["trbl"][i][j] = 1
                elif i > 0 and j < m - 1:
                    prev_len = dp_in["trbl"][i - 1][j + 1]
                    if prev_len > 0 and grid[i][j] == get_expected_val(prev_len + 1):
                        dp_in["trbl"][i][j] = prev_len + 1
        for i in range(n - 1, -1, -1):
            for j in range(m):
                if grid[i][j] == 1:
                    dp_in["bltr"][i][j] = 1
                elif i < n - 1 and j > 0:
                    prev_len = dp_in["bltr"][i + 1][j - 1]
                    if prev_len > 0 and grid[i][j] == get_expected_val(prev_len + 1):
                        dp_in["bltr"][i][j] = prev_len + 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if grid[i][j] == 1:
                    dp_in["brtl"][i][j] = 1
                elif i < n - 1 and j < m - 1:
                    prev_len = dp_in["brtl"][i + 1][j + 1]
                    if prev_len > 0 and grid[i][j] == get_expected_val(prev_len + 1):
                        dp_in["brtl"][i][j] = prev_len + 1
        
        max_len = 0
        for dir_name in dirs:
            for i in range(n):
                for j in range(m):
                    max_len = max(max_len, dp_in[dir_name][i][j])

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if grid[i][j] == 0:
                    dp_out["tlbr_s0"][i][j] = 1 + (dp_out["tlbr_s2"][i + 1][j + 1] if i < n - 1 and j < m - 1 else 0)
                if grid[i][j] == 2:
                    dp_out["tlbr_s2"][i][j] = 1 + (dp_out["tlbr_s0"][i + 1][j + 1] if i < n - 1 and j < m - 1 else 0)
        for i in range(n - 1, -1, -1):
            for j in range(m):
                if grid[i][j] == 0:
                    dp_out["trbl_s0"][i][j] = 1 + (dp_out["trbl_s2"][i + 1][j - 1] if i < n - 1 and j > 0 else 0)
                if grid[i][j] == 2:
                    dp_out["trbl_s2"][i][j] = 1 + (dp_out["trbl_s0"][i + 1][j - 1] if i < n - 1 and j > 0 else 0)
        for i in range(n):
            for j in range(m - 1, -1, -1):
                if grid[i][j] == 0:
                    dp_out["bltr_s0"][i][j] = 1 + (dp_out["bltr_s2"][i - 1][j + 1] if i > 0 and j < m - 1 else 0)
                if grid[i][j] == 2:
                    dp_out["bltr_s2"][i][j] = 1 + (dp_out["bltr_s0"][i - 1][j + 1] if i > 0 and j < m - 1 else 0)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dp_out["brtl_s0"][i][j] = 1 + (dp_out["brtl_s2"][i - 1][j - 1] if i > 0 and j > 0 else 0)
                if grid[i][j] == 2:
                    dp_out["brtl_s2"][i][j] = 1 + (dp_out["brtl_s0"][i - 1][j - 1] if i > 0 and j > 0 else 0)

        turns = { "tlbr": "trbl", "trbl": "brtl", "brtl": "bltr", "bltr": "tlbr" }

        for i in range(n):
            for j in range(m):
                for in_dir_name, out_dir_name in turns.items():
                    l1 = dp_in[in_dir_name][i][j]
                    if l1 == 0:
                        continue

                    dr, dc = dirs[out_dir_name]
                    
                    if l1 == 1:
                        r, c = i + dr, j + dc
                        if 0 <= r < n and 0 <= c < m and grid[r][c] == 2:
                            l2_part = dp_out[out_dir_name + "_s2"][r][c]
                            max_len = max(max_len, 1 + l2_part)
                    else:
                        val_at_turn = grid[i][j]
                        l2 = 0
                        if val_at_turn == 2:
                            l2 = dp_out[out_dir_name + "_s2"][i][j]
                        else:
                            l2 = dp_out[out_dir_name + "_s0"][i][j]
                        
                        if l2 > 0:
                            max_len = max(max_len, l1 + l2 - 1)
        
        return max_len
