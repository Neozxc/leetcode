class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_sum = max(nums)
        count = 0
        i = 0
        ans = 0

        for j in range(len(nums)):
            if nums[j] == max_sum:
                count += 1

            while count >= k:
                ans += len(nums) - j

                if nums[i] == max_sum:
                    count -= 1

                i += 1

        return ans
