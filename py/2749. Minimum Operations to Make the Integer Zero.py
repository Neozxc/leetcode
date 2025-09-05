class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 62):
            target = num1 - k * num2

            if k <= target and target.bit_count() <= k:
                return k

        return - 1
