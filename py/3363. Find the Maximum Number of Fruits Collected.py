class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        if n == 0:
            return 0

        total_fruits = 0
        extra_fruits = [[0] * n for _ in range(n)]
        for i in range(n):
            total_fruits += fruits[i][i]
            for j in range(n):
                if i != j:
                    extra_fruits[i][j] = fruits[i][j]

        dp2_prev = [-1] * n
        dp2_prev[n - 1] = extra_fruits[0][n-1] if 0 != n - 1 else 0

        for s in range(1, n):
            dp2_curr = [-1] * n
            for j in range(s, n):
                max_prev_score = -1
                for dj in [-1, 0, 1]:
                    prev_j = j - dj
                    if s - 1 <= prev_j < n and dp2_prev[prev_j] != -1:
                        max_prev_score = max(max_prev_score, dp2_prev[prev_j])
                
                if max_prev_score != -1:
                    dp2_curr[j] = extra_fruits[s][j] + max_prev_score
            dp2_prev = dp2_curr
        
        if dp2_prev[n - 1] > 0:
            total_fruits += dp2_prev[n-1]

        dp3_prev = [-1] * n
        dp3_prev[n - 1] = extra_fruits[n - 1][0] if n - 1 != 0 else 0

        for s in range(1, n):
            dp3_curr = [-1] * n
            for i in range(s, n):
                max_prev_score = -1
                for di in [-1, 0, 1]:
                    prev_i = i - di
                    if s - 1 <= prev_i < n and dp3_prev[prev_i] != -1:
                        max_prev_score = max(max_prev_score, dp3_prev[prev_i])

                if max_prev_score != -1:
                    dp3_curr[i] = extra_fruits[i][s] + max_prev_score
            dp3_prev = dp3_curr
            
        if dp3_prev[n - 1] > 0:
            total_fruits += dp3_prev[n-1]

        return total_fruits
