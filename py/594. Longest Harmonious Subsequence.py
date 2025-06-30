class Solution:
    def findLHS(self, nums: List[int]) -> int:
        x = Counter(nums)
        y = 0

        for num in nums:
            if num + 1 in x:
                c = x[num] + x[num + 1]
                y = max(y, c)

        return y
 