class Solution:
    def maxDifference(self, s: str) -> int:
        char_freq = [0] * 26

        for char_code in s:
            index = ord(char_code) - ord('a')
            char_freq[index] += 1

        max_odd_value = -1
        min_even_value = 101

        for freq in char_freq:
            if freq == 0:
                continue
            
            if freq % 2 == 1:
                if freq > max_odd_value:
                    max_odd_value = freq
            else:
                if freq < min_even_value:
                    min_even_value = freq

        return max_odd_value - min_even_value
