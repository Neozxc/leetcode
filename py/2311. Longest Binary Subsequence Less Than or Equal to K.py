class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        length = 0
        val = 0
        power = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                length += 1
            else:
                if val + power <= k:
                    val += power
                    length += 1

            if power <= k:
                power *= 2

        return length
