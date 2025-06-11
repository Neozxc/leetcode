class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        overall_max_ans = -math.inf
        
        pref_counts = [[0] * (n + 1) for _ in range(5)]
        for char_code in range(5):
            for i in range(1, n + 1):
                pref_counts[char_code][i] = pref_counts[char_code][i-1]
                if int(s[i-1]) == char_code:
                    pref_counts[char_code][i] += 1

        for ac in range(5):
            for bc in range(5):
                if ac == bc:
                    continue
                
                min_info_at_state = {} 
                max_diff_for_pair = -math.inf

                for j_idx in range(k - 1, n):
                    current_end_prefix_len = j_idx + 1
                    
                    prefix_to_update_state_len = current_end_prefix_len - k
                    
                    ca_start_cand = pref_counts[ac][prefix_to_update_state_len]
                    cb_start_cand = pref_counts[bc][prefix_to_update_state_len]
                    
                    P_val_start_cand = ca_start_cand - cb_start_cand
                    par_a_start_cand = ca_start_cand % 2
                    par_b_start_cand = cb_start_cand % 2
                    state_at_start_cand = (par_a_start_cand, par_b_start_cand)
                    
                    current_min_P, current_cb_for_min_P = min_info_at_state.get(state_at_start_cand, (math.inf, math.inf))
                    
                    if P_val_start_cand < current_min_P:
                        min_info_at_state[state_at_start_cand] = (P_val_start_cand, cb_start_cand)
                    elif P_val_start_cand == current_min_P:
                        min_info_at_state[state_at_start_cand] = (P_val_start_cand, min(current_cb_for_min_P, cb_start_cand))

                    ca_end_prefix = pref_counts[ac][current_end_prefix_len]
                    cb_end_prefix = pref_counts[bc][current_end_prefix_len]
                    P_val_end_prefix = ca_end_prefix - cb_end_prefix
                    par_a_end_prefix = ca_end_prefix % 2
                    par_b_end_prefix = cb_end_prefix % 2
                    
                    req_par_a_for_start = (par_a_end_prefix - 1 + 2) % 2
                    req_par_b_for_start = par_b_end_prefix
                    required_start_state = (req_par_a_for_start, req_par_b_for_start)
                    
                    retrieved_min_P_start, retrieved_cb_start = min_info_at_state.get(required_start_state, (math.inf, math.inf))

                    if retrieved_min_P_start != math.inf:
                        count_b_in_substring = cb_end_prefix - retrieved_cb_start
                        if count_b_in_substring > 0: 
                            current_diff = P_val_end_prefix - retrieved_min_P_start
                            max_diff_for_pair = max(max_diff_for_pair, current_diff)
                
                if max_diff_for_pair != -math.inf:
                    overall_max_ans = max(overall_max_ans, max_diff_for_pair)

        return overall_max_ans if overall_max_ans != -math.inf else -1
