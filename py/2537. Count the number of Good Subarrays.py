class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        total_pairs = 0
        left = 0
        answer = 0

        for right in range(len(nums)):
            num = nums[right]

            total_pairs += freq[num]
            freq[num] += 1

            while total_pairs >= k:
                answer += len(nums) - right

                freq[nums[left]] -= 1
                total_pairs -= freq[nums[left]]
                left += 1

        return answer
