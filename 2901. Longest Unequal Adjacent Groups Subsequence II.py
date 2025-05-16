class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [1] * n
        parent = [-1] * n

        for i in range(n):
            for j in range(i):
                if (
                    groups[i] != groups[j]
                    and self.hamming_distance(words[i], words[j])
                    and dp[j] + 1 > dp[i]
                ):
                    dp[i] = dp[j] + 1
                    parent[i] = j

        max_len = max(dp)
        end_idx = dp.index(max_len)

        result = []
        while end_idx != -1:
            result.append(words[end_idx])
            end_idx = parent[end_idx]

        return result[::-1]

    def hamming_distance(self, w1, w2):
        if len(w1) != len(w2):
            return False
        diff = 0
        for a, b in zip(w1, w2):
            if a != b:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1
