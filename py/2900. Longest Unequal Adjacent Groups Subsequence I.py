class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        last0 = []
        last1 = []

        for word, group in zip(words, groups):
            if group == 0:
                if len(last1) + 1 > len(last0):
                    last0 = last1 + [word]
                else:
                    last0 = last0
            else:
                if len(last0) + 1 > len(last1):
                    last1 = last0 + [word]
                else:
                    last1 = last1

        return last0 if len(last0) > len(last1) else last1
