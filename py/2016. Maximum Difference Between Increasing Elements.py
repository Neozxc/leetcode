class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_so_far = float('inf')
        max_diff = -1

        for current_num in nums:
            if current_num > min_so_far:
                diff = current_num - min_so_far

                if diff > max_diff:
                    max_diff = diff

            if current_num < min_so_far:
                min_so_far = current_num

        return max_diff
