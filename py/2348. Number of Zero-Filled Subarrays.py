class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        sub, zeros = 0, 0 

        for num in nums:
            if num == 0:
                zeros += 1
            else:
                zeros = 0

            sub += zeros

        return sub
