class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        mod = modulo
        shift = (mod - k) % mod
        freq = {0: 1}
        freq_get = freq.get
        count = 0
        prefix_mod = 0

        for num in nums:
            if num % mod == k:
                prefix_mod += 1

                if prefix_mod == mod:
                    prefix_mod = 0

            target = prefix_mod + shift

            if target >= mod:
                target -= mod

            count += freq_get(target, 0)

            freq[prefix_mod] = freq_get(prefix_mod, 0) + 1

        return count
