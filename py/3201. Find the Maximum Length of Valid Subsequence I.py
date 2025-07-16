class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count_even = 0
        count_odd = 0
        len_alterating = 0
        last_parity = -1

        for num in nums:
            parity = num % 2
            
            if parity == 0:
                count_even += 1
            else:
                count_odd += 1

            if parity != last_parity:
                len_alterating += 1
                last_parity = parity

        return max(count_even, count_odd, len_alterating)
