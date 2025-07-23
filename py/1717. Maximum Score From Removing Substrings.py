class Solution:
    def maximumGain(sel, s: str, x: int, y: int) -> int:
        def removePairs(pair, score):
            nonlocal s
            res = 0
            stack = []

            for c in s:
                if c == pair[1] and stack and stack[-1] == pair[0]:
                    stack.pop()
                    res += score
                else:
                    stack.append(c)

            s = "".join(stack)

            return res


        res = 0
        pair = "ab" if x > y else "ba"
        res += removePairs(pair, max(x, y))
        res += removePairs(pair[::-1], min(x, y))

        return res
