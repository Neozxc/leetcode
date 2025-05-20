class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)

        for left, right in queries:
            diff[left] += 1
            if right + 1 < len(diff):
                diff[right + 1] -= 1

        coverage = [0] * n
        coverage[0] = diff[0]
        for i in range(1, n):
            coverage[i] = coverage[i - 1] + diff[i]

        for i in range(n):
            if nums[i] > coverage[i]:
                return False

        return True
