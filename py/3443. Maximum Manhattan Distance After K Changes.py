class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        n = len(s)
        max_overall_manhattan_dist = 0

        num_N, num_S, num_E, num_W = 0, 0, 0, 0

        for i in range(n):
            char = s[i]
            if char == 'N':
                num_N += 1
            elif char == 'S':
                num_S += 1
            elif char == 'E':
                num_E += 1
            elif char == 'W':
                num_W += 1
            
            N_U_plus = num_N + num_E
            N_U_minus = num_S + num_W

            val_max_U = (N_U_plus - N_U_minus) + 2 * min(k, N_U_minus)
            val_max_neg_U = (N_U_minus - N_U_plus) + 2 * min(k, N_U_plus)

            N_V_plus = num_S + num_E
            N_V_minus = num_N + num_W
            
            val_max_V = (N_V_plus - N_V_minus) + 2 * min(k, N_V_minus)
            val_max_neg_V = (N_V_minus - N_V_plus) + 2 * min(k, N_V_plus)
            
            current_prefix_max_dist = max(val_max_U, val_max_neg_U, val_max_V, val_max_neg_V)
            
            max_overall_manhattan_dist = max(max_overall_manhattan_dist, current_prefix_max_dist)
            
        return max_overall_manhattan_dist
