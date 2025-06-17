class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        def power(base, exp):
            res = 1
            base %= MOD
            while exp > 0:
                if exp % 2 == 1:
                    res = (res * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return res

        max_val = n
        fact = [1] * (max_val + 1)
        inv_fact = [1] * (max_val + 1)
        
        for i in range(1, max_val + 1):
            fact[i] = (fact[i - 1] * i) % MOD
        
        inv_fact[max_val] = power(fact[max_val], MOD - 2)
        
        for i in range(max_val, 0, -1):
            inv_fact[i - 1] = (inv_fact[i] * i) % MOD

        def combinations(n_val, k_val):
            if k_val < 0 or k_val > n_val:
                return 0
            numerator = fact[n_val]
            denominator = (inv_fact[k_val] * inv_fact[n_val - k_val]) % MOD
            return (numerator * denominator) % MOD

        ways_to_choose_positions = combinations(n - 1, k)
        ways_to_fill_mismatches = power(m - 1, n - 1 - k)
        
        ans = (m * ways_to_choose_positions) % MOD
        ans = (ans * ways_to_fill_mismatches) % MOD
        
        return ans
