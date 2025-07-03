class Solution:
    def kthCharacter(self, k: int) -> str:
        j = k - 1
        num = bin(j).count('1')
        num_ord = ord('a') + num

        return chr(num_ord)
