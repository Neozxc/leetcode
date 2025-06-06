class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)

        min_suffix = [''] * n
        min_suffix[n - 1] = s[n - 1]

        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(s[i], min_suffix[i + 1])

        paper_chars = []
        t_stack = []

        for i in range(n):
            current_s_char = s[i]

            while t_stack and t_stack[-1] <= min_suffix[i]:
                paper_chars.append(t_stack.pop())

            t_stack.append(current_s_char)

        while t_stack:
            paper_chars.append(t_stack.pop())

        return "".join(paper_chars)
