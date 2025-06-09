class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        current_max_sum = 0
        nodes_flipped_count = 0
        min_sacrifice_to_fix_parity = float('inf')

        for nums_val in nums:
            num_val_xored_k = nums_val ^ k

            if num_val_xored_k > nums_val:
                current_max_sum += num_val_xored_k
                nodes_flipped_count += 1
            else:
                current_max_sum += nums_val

            sacrifice_for_this_node = abs(num_val_xored_k - nums_val)
            min_sacrifice_to_fix_parity = min(min_sacrifice_to_fix_parity, sacrifice_for_this_node)

        if nodes_flipped_count % 2 == 0:
            return current_max_sum
        else:
            return current_max_sum - min_sacrifice_to_fix_parity
