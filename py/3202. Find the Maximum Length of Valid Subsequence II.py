class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        max_len = 0

        for num in nums:
            current_rem = num % k
            for prev_rem in range(k):
                dp[prev_rem][current_rem] = dp[current_rem][prev_rem] + 1
                max_len = max(max_len, dp[prev_rem][current_rem])

        return max_len
