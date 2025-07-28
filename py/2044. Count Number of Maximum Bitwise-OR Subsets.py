class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0

        for num in nums:
            max_or |= num
        
        self.count = 0
        n = len(nums)
        
        def backtrack(index: int, current_or: int):
            if index == n:
                if current_or == max_or:
                    self.count += 1
                return
            
            backtrack(index + 1, current_or)
            backtrack(index + 1, current_or | nums[index])

        backtrack(0, 0)
        
        return self.count
