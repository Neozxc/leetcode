class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9+7
        dp = [0] * (n + 1)
        dp[1] = 1
        share_count = 0

        for i in range(2, n + 1):
            if i - delay >= 1:
                share_count = (share_count + dp[i - delay]) % MOD

            if i - forget >= 1:
                share_count = (share_count - dp[i - forget] + MOD) % MOD

            dp[i] = share_count

        res = 0

        for i in range(n - forget + 1, n + 1):
            if i >= 1:
                res = (res + dp[i]) % MOD

        return res
