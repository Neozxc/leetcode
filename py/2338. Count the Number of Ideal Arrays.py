class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9+7
        maxLen = 14

        dp = [[0] * (maxLen + 1) for _ in range(maxValue + 1)]

        for i in range(1, maxValue + 1):
            dp[i][1] = 1

        for length in range(2, maxLen + 1):
            for i in range(1, maxValue + 1):
                for j in range(i * 2, maxValue + 1, i):
                    dp[j][length] = (dp[j][length] + dp[i][length - 1]) % MOD

        result = 0

        for val in range(1, maxValue + 1):
            for k in range(1, maxLen + 1):
                if dp[val][k] == 0:
                    continue

                ways = comb(n - 1, k - 1)
                result = (result + dp[val][k] * ways) % MOD

        return result
