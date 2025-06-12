class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        max_diff = 0

        for i in range(n):
            current = nums[i]
            next_element = nums[(i + 1) % n]
            difference = abs(current - next_element)

            if difference > max_diff:
                max_diff = difference

        return max_diff
