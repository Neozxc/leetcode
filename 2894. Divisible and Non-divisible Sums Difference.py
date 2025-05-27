class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum_diff = 0
        
        for i in range(1, n + 1):
            if i % m == 0:
                sum_diff -= i
            else:
                sum_diff += i

        return sum_diff
