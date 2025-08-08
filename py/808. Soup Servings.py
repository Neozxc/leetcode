class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1.0

        @lru_cache(maxsize=None)
        def solve(a: int, b: int ) -> float:
            if a <= 0 and b <= 0:
                return 0.5

            if a <= 0:
                return 1.0

            if b <= 0:
                return 0.0

            p1 = solve(a - 4, b)
            p2 = solve(a - 3, b - 1)
            p3 = solve(a - 2, b - 2)
            p4 = solve(a - 1, b - 3)

            return 0.25 * (p1 + p2 + p3 + p4)

        N = math.ceil(n / 25)

        return solve(N, N)
