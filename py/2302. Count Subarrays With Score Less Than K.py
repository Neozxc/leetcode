class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        window_sum = 0
        result = 0

        for i in range(len(nums)):
            window_sum += nums[i]

            while window_sum * (i - left + 1) >= k:
                window_sum -= nums[left]
                left += 1

            result += (i - left + 1)

        return result
