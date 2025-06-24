class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)

        key_indeces = []

        for i in range(n):
            if nums[i] == key:
                key_indeces.append(i)

        result = []
        last_painted_index = -1

        for j in key_indeces:
            start = max(0, j - k)
            end = min(n - 1, j + k)

            paint_from = max(start, last_painted_index + 1)
            
            for i in range(paint_from, end + 1):
                result.append(i)

            last_painted_index = max(last_painted_index, end)

        return result
