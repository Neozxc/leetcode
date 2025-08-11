class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9+7
        powers = []
        
        for i in range(32):
            if (n >> i) & 1:
                powers.append(2**i)

        prefix_prod = [1] * (len(powers) + 1)

        for i in range(len(powers)):
            prefix_prod[i + 1] = (prefix_prod[i] * powers[i]) % MOD

        ans = []

        for left, right in queries:
            num = prefix_prod[right + 1]
            deno = prefix_prod[left]

            inv = pow(deno, MOD - 2, MOD)
            res = (num * inv) % MOD

            ans.append(res)

        return ans
