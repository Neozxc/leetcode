class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        A = [[0]*26 for _ in range(26)]

        for i in range(26):
            for d in range(1, nums[i] + 1):
                A[i][(i + d) % 26] += 1

        def mat_mult(X, Y):
            Z = [[0]*26 for _ in range(26)]
            for i in range(26):
                Xi = X[i]
                Zi = Z[i]
                for k in range(26):
                    v = Xi[k]
                    if v:
                        Yk = Y[k]
                        for j in range(26):
                            Zi[j] = (Zi[j] + v * Yk[j]) % MOD
            return Z

        def mat_pow(mat, power):
            res = [[int(i == j) for j in range(26)] for i in range(26)]
            while power:
                if power & 1:
                    res = mat_mult(res, mat)
                mat = mat_mult(mat, mat)
                power >>= 1
            return res

        At = mat_pow(A, t)

        ft = [sum(row) % MOD for row in At]

        ans = 0

        for ch in s:
            ans = (ans + ft[ord(ch) - ord('a')]) % MOD

        return ans
