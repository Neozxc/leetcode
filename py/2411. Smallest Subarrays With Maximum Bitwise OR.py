class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        last_seen = [-1] * 30

        for i in range(n - 1, - 1, - 1):
            for b in range(30):
                if (nums[i] >> b) & 1:
                    last_seen[b] = i

            end_j = i
            for b_idx in last_seen:
                end_j = max(end_j, b_idx)

            ans[i] = end_j - i + 1

        return ans
