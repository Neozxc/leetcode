class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        window = set()
        current = 0
        max_score = 0

        for right in range(len(nums)):
            while nums[right] in window:
                current -= nums[left]
                window.remove(nums[left])
                left += 1

            window.add(nums[right])
            current += nums[right]

            max_score = max(max_score, current)

        return max_score
