class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        length = 0 
        current = 0

        for num in nums:
            if num == max_val:
                current += 1
            else:
                current = 0

            length = max(length, current)

        return length
