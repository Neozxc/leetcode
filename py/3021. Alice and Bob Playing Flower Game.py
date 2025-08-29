class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        n_even = n // 2
        n_odd = (n + 1) // 2
        
        m_even = m // 2
        m_odd = (m + 1) // 2

        return (n_even * m_odd) + (m_even * n_odd)
