class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        counts = Counter(s)
        possible_chars = sorted([char for char, freq in counts.items() if freq >= k])
        queue = deque([""])
        answer = ""

        while queue:
            curr = queue.popleft()

            for char in possible_chars:
                new_candidate = curr + char

                if self.is_subsequence(s, new_candidate * k):
                    answer = new_candidate
                    queue.append(new_candidate)

        return answer
    
    def is_subsequence(self, text, target):
        it = iter(text)
        return all(c in it for c in target)
