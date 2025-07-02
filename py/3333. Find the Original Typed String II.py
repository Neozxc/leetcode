class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7

        if not word:
            return 0
        
        groups = []
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)

        m = len(groups)
        
        total_ways = 1
        for g in groups:
            total_ways = (total_ways * g) % MOD
            
        if k <= m:
            return total_ways

        h_len = k - m
        
        counts = collections.Counter(groups)
        inv = self._get_inverses(h_len, MOD)


        i_times_a = [0] * h_len
        for v, num_v in counts.items():
            val = v * num_v 
            for i in range(v, h_len, v):
                i_times_a[i] -= val
        
        f = self._poly_exp(i_times_a, h_len, MOD, inv)
        
        m_mod = m % MOD
        i_times_b = [m_mod] * h_len
        i_times_b[0] = 0
            
        g = self._poly_exp(i_times_b, h_len, MOD, inv)
        
        h = [0] * h_len
        for j in range(h_len):
            val = 0
            for i in range(j + 1):
                val += f[i] * g[j - i]
            h[j] = val % MOD

        count_less = sum(h) % MOD
            
        return (total_ways - count_less + MOD) % MOD
        
    def _get_inverses(self, n, mod):
        if n <= 1:
            return [0] * n
        inv = [0] * n
        inv[1] = 1
        for i in range(2, n):
            inv[i] = mod - (mod // i) * inv[mod % i] % mod
        return inv

    def _poly_exp(self, i_times_deriv_coeffs, n, mod, inv):
        f = [0] * n
        if n > 0:
            f[0] = 1
        for i in range(1, n):
            sum_val = 0
            for j in range(1, i + 1):
                term = (i_times_deriv_coeffs[j]) * f[i - j]
                sum_val += term
            f[i] = (sum_val % mod * inv[i]) % mod

        return f
