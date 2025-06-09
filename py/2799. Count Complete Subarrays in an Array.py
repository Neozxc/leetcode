# Time: O(n^2) Beats 5%
# Space: O(n) Beats 95%
# Need to find better solution, this is too slow

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_unique = len(set(nums))
        n = len(nums)
        count = 0

        for start in range(n):
            freq = defaultdict(int)
            unique = 0

            for end in range(start, n):
                if freq[nums[end]] == 0:
                    unique += 1
                freq[nums[end]] += 1

                if unique == total_unique:
                    count += 1
        
        return count
